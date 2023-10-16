from oarepo_model_builder.datatypes.components import (
    DefaultsModelComponent,
    RecordModelComponent,
)
from oarepo_model_builder.datatypes.components.model.record_metadata import (
    RecordMetadataModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import set_default

from oarepo_model_builder_communities.datatypes import RecordCommunitiesDataType


class RecordCommunitiesMetadataModelComponent(RecordMetadataModelComponent):
    eligible_datatypes = [RecordCommunitiesDataType]
    depends_on = [DefaultsModelComponent, RecordModelComponent]
    affects = [RecordMetadataModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        metadata = set_default(datatype, "record-metadata", {})
        metadata.setdefault(
            "base-classes",
            ["db.Model", "CommunityRelationMixin"],
        )
        metadata.setdefault(
            "imports",
            [
                {"import": "invenio_db.db"},
                {
                    "import": "invenio_communities.records.records.models.CommunityRelationMixin"
                },
            ],
        )
        metadata.setdefault(
            "module",
            context["published_record"].definition["record-metadata"]["module"],
        )
        metadata.setdefault("use-versioning", False)
        super().before_model_prepare(datatype, context=context, **kwargs)
