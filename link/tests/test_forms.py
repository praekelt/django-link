from django.test import TestCase

from link import forms


class FormTestCase(TestCase):
    def setUp(self):
        self.form_data = {
            "title": "Link 1 Title",
            "slug": "link-1-title"
        }

    def test_admin_form(self):

        # ensure that not selecting a target raises a validation error
        admin_form = forms.LinkAdminForm(self.form_data)
        admin_form.full_clean()
        self.assertEqual(len(admin_form.errors["__all__"]), 1)

        # ensure the form is valid
        self.form_data["url"] = "/test-link/"
        admin_form = forms.LinkAdminForm(self.form_data)
        self.assertTrue(admin_form.is_valid())
        self.assertEqual(len(admin_form.errors), 0)

        # ensure that selecting multiple targets fails
        self.form_data["view_name"] = "link-1"
        admin_form = forms.LinkAdminForm(self.form_data)
        admin_form.full_clean()
        self.assertEqual(len(admin_form.errors["__all__"]), 1)

    def tearDown(self):
        pass
