from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.editor = get_user_model().objects.create(
            username="editor",
            email="editor@test.com",
            is_superuser=True,
            is_staff=True
        )
        self.editor.set_password("password")
        self.editor.save()
        self.client.login(username="editor", password="password")

    def test_admin(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_admin_link(self):

        # ensure the link add page can be reached
        response = self.client.get("/admin/link/link/add/")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
