from django.test import TestCase
from django.test.client import Client

from link import models


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.link_data = {
            "title": "Link 1 Title",
            "slug": "link-1-title",
            "url": "/link-1/"
        }
        self.link = models.Link.objects.create(**self.link_data)

    def test_detail(self):
        response = self.client.get("/link/%s/" % self.link_data["slug"])
        self.assertContains(response, self.link_data["title"])

    def test_list(self):
        link_data2 = {
            "title": "Link 2 Title",
            "slug": "link-2-title",
            "url": "/link-2/"
        }
        models.Link.objects.create(**link_data2)

        response = self.client.get("/link/")
        self.assertContains(response, self.link_data["title"])
        self.assertContains(response, link_data2["title"])

    def tearDown(self):
        pass
