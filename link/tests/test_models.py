from django.test import TestCase

from link import models


class ModelTestCase(TestCase):
    def setUp(self):
        self.link_data = {
            "title": "Link 1 Title",
            "url": "/link-1/"
        }
        self.viewparam_data = {
            "key": "slug",
            "value": "1",
        }

    def test_link(self):
        link = models.Link.objects.create(**self.link_data)

        # ensure the data was saved correctly
        for key, value in self.link_data.items():
            self.assertEqual(getattr(link, key), value)

        # ensure get_absolute_url returns the correct string
        self.assertEqual(link.absolute_url, "/link-1/")

        # ensure that links with view names selected render the correct string
        link.view_name = "link-2"
        self.assertEqual(link.absolute_url, "/link/2/")

        # ensure that links with target objects render the correct string
        content_link_data = self.link_data.copy()
        content_link_data["url"] = "/content/1/"
        content_link = models.Link.objects.create(**content_link_data)
        link.view_name = None
        link.target = content_link
        self.assertEqual(link.absolute_url, "/content/1/")

    def test_viewparam(self):
        link = models.Link.objects.create(**self.link_data)
        viewparam = models.ViewParam.objects.create(**self.viewparam_data)
        link.view_params.add(viewparam)
        link.view_name = "link:link-detail"

        # ensure the url is returned correctly
        self.assertEqual(link.absolute_url, "/link/1/")
