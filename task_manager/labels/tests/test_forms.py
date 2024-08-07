from task_manager.labels.forms import LabelCreateForm
from .testcase import LabelTestCase


class LabelFormTest(LabelTestCase):
    def test_valid_form(self) -> None:
        label_data = self.test_label['create']['valid'].copy()
        form = LabelCreateForm(data=label_data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self) -> None:
        label_data = self.test_label['create']['missing_fields'].copy()
        form = LabelCreateForm(data=label_data)

        self.assertFalse(form.is_valid())
