import marshmallow as ma
from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, Section
from oarepo_model_builder.datatypes.components import DefaultsModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import base_name


def get_record_communities_schema():
    from ..communities import RecordCommunitiesDataType

    return RecordCommunitiesDataType.validator()


class RecordCommunitiesComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    affects = [DefaultsModelComponent]

    class ModelSchema(ma.Schema):
        draft_files = ma.fields.Nested(
            get_record_communities_schema,
            data_key="record-communities",
            attribute="record-communities",
        )

    def process_links(self, datatype, section: Section, **kwargs):
        if datatype.root.profile == "record_communities":
            section.config = {}

    def process_mb_invenio_drafts_parent_record(
        self, datatype, section: Section, **kwargs
    ):
        if "record-communities" in datatype.definition:
            record_communities_record = datatype.schema.get_schema_section(
                "record_communities",
                ["record", "record-communities"],
                prepare_context={
                    "profile": "record_communities",
                    "published_record": datatype.schema.get_schema_section(
                        "record", ["record"]
                    ),
                    "profile_module": "record_communities",
                },
            )
            additional_parent_fields = {}
            additional_parent_fields["additional-fields"] = [
                f"communities = CommunitiesField({base_name(record_communities_record.definition['record-metadata']['class'])})"
            ]

            additional_parent_fields["imports"] = [
                {
                    "import": "invenio_communities.records.records.systemfields.CommunitiesField"
                },
                {
                    "import": record_communities_record.definition["record-metadata"][
                        "class"
                    ],
                },
            ]
            section.config["additional-parent-fields"] = additional_parent_fields

    def process_mb_invenio_drafts_record_communities_service_config(
        self, datatype, section: Section, **kwargs
    ):
        if "record-communities" in datatype.definition:
            record_communities_record = datatype.schema.get_schema_section(
                "record_communities",
                ["record", "record-communities"],
                prepare_context={
                    "profile": "record_communities",
                    "published_record": datatype.schema.get_schema_section(
                        "record", ["record"]
                    ),
                    "profile_module": "record_communities",
                },
            )
            section.config[
                "record-communities-service-config"
            ] = record_communities_record.definition["service-config"]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if datatype.root.profile == "record_communities":
            set_default(datatype, "search-options", {}).setdefault("skip", True)
            set_default(datatype, "permissions", {}).setdefault("skip", True)
