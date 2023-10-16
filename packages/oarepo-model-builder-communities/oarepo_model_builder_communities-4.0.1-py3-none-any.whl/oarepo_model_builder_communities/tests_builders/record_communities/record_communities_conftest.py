from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class RecordCommunitiesConftestBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "record_communities_conftest"
    template = "record-communities-conftest"

    def _get_output_module(self):
        return f'{self.current_model.definition["tests"]["module"]}.record_communities.conftest'

    def finish(self, **extra_kwargs):
        tests = getattr(self.current_model, "section_tests")
        super().finish(
            fixtures=tests.fixtures, test_constants=tests.constants, **extra_kwargs
        )
