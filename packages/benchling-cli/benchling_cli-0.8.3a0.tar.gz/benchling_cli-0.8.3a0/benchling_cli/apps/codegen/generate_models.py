from typing import Dict, Optional, Union

from benchling_api_client.v2.beta.models.benchling_app_manifest import BenchlingAppManifest
from benchling_api_client.v2.beta.models.dropdown_dependency import DropdownDependency
from benchling_api_client.v2.beta.models.entity_schema_dependency import EntitySchemaDependency
from benchling_api_client.v2.beta.models.manifest_float_scalar_config import ManifestFloatScalarConfig
from benchling_api_client.v2.beta.models.manifest_integer_scalar_config import ManifestIntegerScalarConfig
from benchling_api_client.v2.beta.models.manifest_text_scalar_config import ManifestTextScalarConfig
from benchling_api_client.v2.beta.models.schema_dependency import SchemaDependency
from benchling_api_client.v2.beta.models.schema_dependency_subtypes import SchemaDependencySubtypes
from benchling_api_client.v2.beta.models.workflow_task_schema_dependency import WorkflowTaskSchemaDependency
from benchling_api_client.v2.stable.extensions import NotPresentError
from benchling_sdk.apps.helpers.config_helpers import (
    field_definitions_from_dependency,
    is_config_multi_valued_or_unset,
    is_config_required,
    is_field_value_required,
    model_type_from_dependency,
    options_from_dependency,
    scalar_type_from_field_config,
    workflow_task_schema_output_from_dependency,
)
from jinja2 import Environment, PackageLoader

from benchling_cli.apps.codegen.generate_dependencies_module import _scalar_type_name
from benchling_cli.apps.codegen.helpers import (
    dependency_to_pascal_case,
    dependency_to_snake_case,
    field_type_from_field_definition,
    reformat_code_str,
    to_enum_option,
    to_snake_case,
)


def generate_model(
    dependency: Union[
        DropdownDependency,
        EntitySchemaDependency,
        SchemaDependency,
        WorkflowTaskSchemaDependency,
        ManifestTextScalarConfig,
        ManifestFloatScalarConfig,
        ManifestIntegerScalarConfig,
    ]
) -> str:
    env = Environment(
        loader=PackageLoader("benchling_cli.apps.codegen", "templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if isinstance(dependency, (EntitySchemaDependency, SchemaDependency)):
        template = env.get_template("schema_instance_model.py.jinja2")
    elif isinstance(dependency, WorkflowTaskSchemaDependency):
        template = env.get_template("workflow_instance_model.py.jinja2")
    elif isinstance(dependency, DropdownDependency):
        template = env.get_template("dropdown_model.py.jinja2")
    else:
        template = env.get_template("enum_scalar_model.py.jinja2")

    rendered_template = template.render(
        dependency=dependency,
        dependency_to_pascal_case=dependency_to_pascal_case,
        dependency_to_snake_case=dependency_to_snake_case,
        field_type_from_field_definition=field_type_from_field_definition,
        is_config_required=is_config_required,
        is_config_multi_valued_or_unset=is_config_multi_valued_or_unset,
        model_type_from_dependency=model_type_from_dependency,
        scalar_type_from_field_config=scalar_type_from_field_config,
        scalar_type_name=_scalar_type_name,
        to_snake_case=to_snake_case,
        workflow_task_schema_output_from_dependency=workflow_task_schema_output_from_dependency,
        is_field_value_required=is_field_value_required,
        to_enum_option=to_enum_option,
    )

    return reformat_code_str(rendered_template)


def generate_models(manifest: BenchlingAppManifest) -> Dict[str, str]:
    assert manifest.configuration
    return {
        dependency_to_snake_case(dependency): generate_model(dependency)
        for dependency in manifest.configuration
        if (
            (
                isinstance(
                    dependency,
                    (SchemaDependency, DropdownDependency, WorkflowTaskSchemaDependency),
                )
                or (isinstance(dependency, EntitySchemaDependency) and _entity_schema_has_subtype(dependency))
            )
            and _has_subdependencies(dependency)
        )
        or (
            isinstance(
                dependency, (ManifestTextScalarConfig, ManifestFloatScalarConfig, ManifestIntegerScalarConfig)
            )
            and _is_enumerated_type(dependency)
        )
    }


def _is_enumerated_type(dependency) -> bool:
    if isinstance(
        dependency, (ManifestTextScalarConfig, ManifestFloatScalarConfig, ManifestIntegerScalarConfig)
    ):
        try:
            if hasattr(dependency, "enum"):
                return True
        # We can't seem to handle this programmatically by checking isinstance() or field truthiness
        except NotPresentError:
            pass
    return False


def _has_subdependencies(dependency) -> bool:
    return (
        isinstance(dependency, (WorkflowTaskSchemaDependency, EntitySchemaDependency, SchemaDependency))
        and bool(field_definitions_from_dependency(dependency))
    ) or (isinstance(dependency, DropdownDependency) and bool(options_from_dependency(dependency)))


def _entity_schema_has_subtype(dependency: EntitySchemaDependency) -> Optional[SchemaDependencySubtypes]:
    """Safely return a subtype from an entity schema dependency."""
    try:
        if hasattr(dependency, "subtype"):
            return dependency.subtype
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return None
