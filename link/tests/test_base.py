from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from link import utils, models


class UtilsTestCase(TestCase):
    def test_get_view_names(self):
        self.assertEqual(utils.get_view_names(), ["link-1", "link-2"])


class ModelTestCase(TestCase):
    def setUp(self):
        self.link_data = {
            "title": "Link 1 Title",
            "subtitle": "Link 1 Subtitle",
            "url": "/link-1/"
        }

    def test_link(self):
        link = models.Link.objects.create(**self.link_data)

        # ensure the data was saved correctly
        for key, value in self.link_data.items():
            self.assertEqual(getattr(link, key), value)

        # ensure get_absolute_url returns the correct string
        self.assertEqual(link.get_absolute_url(), "/link-1/")

        # ensure that links with view names selected render the correct string
        link.view_name = "link-2"
        self.assertEqual(link.get_absolute_url(), "/link/2/")

        # ensure that links with target objects render the correct string
        content_link_data = self.link_data.copy()
        content_link_data["url"] = "/content/1/"
        content_link = models.Link.objects.create(**content_link_data)
        link.view_name = None
        link.target = content_link
        self.assertEqual(link.get_absolute_url(), "/content/1/")
