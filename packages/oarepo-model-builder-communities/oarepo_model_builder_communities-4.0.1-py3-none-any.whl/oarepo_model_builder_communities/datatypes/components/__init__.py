from .record_communities_model import (
    DraftFilesRecordModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesMetadataModelComponent,
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent,
)
from .record_communities_profile import RecordCommunitiesComponent

RECORD_COMMUNITIES_COMPONENTS = [
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent,
    RecordCommunitiesComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    DraftFilesRecordModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesMetadataModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
]
