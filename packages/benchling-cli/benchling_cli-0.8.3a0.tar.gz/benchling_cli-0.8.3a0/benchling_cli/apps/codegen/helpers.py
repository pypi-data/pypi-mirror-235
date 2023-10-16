from dataclasses import dataclass
from keyword import iskeyword
import re
from typing import get_args, List, Optional, Union

from autoflake import fix_code
from benchling_api_client.v2.beta.models.base_manifest_config import BaseManifestConfig
from benchling_api_client.v2.beta.models.benchling_app_manifest import BenchlingAppManifest
from benchling_api_client.v2.beta.models.dropdown_dependency import DropdownDependency
from benchling_api_client.v2.beta.models.entity_schema_dependency import EntitySchemaDependency
from benchling_api_client.v2.beta.models.field_definitions_manifest import FieldDefinitionsManifest
from benchling_api_client.v2.beta.models.manifest_scalar_config import ManifestScalarConfig
from benchling_api_client.v2.beta.models.resource_dependency import ResourceDependency
from benchling_api_client.v2.beta.models.scalar_config_types import ScalarConfigTypes
from benchling_api_client.v2.beta.models.schema_dependency import SchemaDependency
from benchling_api_client.v2.beta.models.workflow_task_schema_dependency import WorkflowTaskSchemaDependency
from benchling_api_client.v2.stable.extensions import NotPresentError, UnknownType
import black


def reformat_code_str(code_str: str) -> str:
    # Use autoflake to remove unused model imports instead of trying to crawl the entire manifest and figure
    # out which ones are being used.
    code_str = fix_code(code_str, remove_all_unused_imports=True)
    return black.format_str(code_str, mode=black.Mode(line_length=110))


DependencyType = Union[
    SchemaDependency,
    DropdownDependency,
    EntitySchemaDependency,
    ResourceDependency,
    ManifestScalarConfig,
    BaseManifestConfig,
    WorkflowTaskSchemaDependency,
]


class UnnamedDependencyError(Exception):
    pass


def _clean_and_split(string: str) -> List[str]:
    remove_symbols = re.sub(r"[\W_]", " ", string)
    insert_space_before_uppercase = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", remove_symbols)
    return insert_space_before_uppercase.split()


def _make_valid_identifier(string: str) -> str:
    # If it starts with a digit, prefix with _
    identifier = re.sub(r"^(?=\d)", "_", string)

    # TODO BNCH-43949 - Expand to prevent interference with code gen mixins (e.g. fields named "name")
    if iskeyword(identifier) or identifier == "self" or identifier in dir(dataclass):
        return f"{identifier}_"
    else:
        return identifier


def to_pascal_case(string: str) -> str:
    return _make_valid_identifier("".join([word.title() for word in _clean_and_split(string)]))


def to_snake_case(string: str) -> str:
    return _make_valid_identifier("_".join([word.lower() for word in _clean_and_split(string)]))


def dependency_to_pascal_case(dependency: DependencyType) -> str:
    if isinstance(dependency, UnknownType) or not hasattr(dependency, "name"):
        raise UnnamedDependencyError(f"No name available for unknown dependency: {dependency}")
    return to_pascal_case(dependency.name)


def dependency_to_snake_case(dependency: DependencyType) -> str:
    if isinstance(dependency, UnknownType) or not hasattr(dependency, "name"):
        raise UnnamedDependencyError(f"No name available for unknown dependency: {dependency}")
    return to_snake_case(dependency.name)


def is_secure_text_dependency(dependency: DependencyType) -> bool:
    return getattr(dependency, "type", None) == ScalarConfigTypes.SECURE_TEXT


def is_manifest_scalar_dependency(dependency: DependencyType) -> bool:
    # Python can't compare isinstance for Union types until Python 3.10 so just do this for now
    # from: https://github.com/python/typing/discussions/1132#discussioncomment-2560441
    return isinstance(dependency, get_args(ManifestScalarConfig))


def field_type_from_field_definition(field: FieldDefinitionsManifest) -> Optional[str]:
    """Return a scalar definition from a manifest field. Defaults to parsing as text."""
    try:
        if hasattr(field, "type") and field.type:
            return field.type
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return None


def to_enum_option(enum_value: Union[str, float, int]) -> str:
    if isinstance(enum_value, (int, float)):
        enum_value = str(enum_value).replace("-", "MINUS_")
    # make all uppercase, remove any symbols, and replace spaces with underscores
    option_value = "_".join([word.upper() for word in _clean_and_split(str(enum_value))]).replace(".", "_")
    return option_value


def manifest_version(manifest: BenchlingAppManifest) -> Optional[str]:
    """Return a version in an App manifest, if present."""
    try:
        if hasattr(manifest, "info") and hasattr(manifest.info, "version") and manifest.info.version:
            return manifest.info.version
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return None
