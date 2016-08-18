# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client, RequestFactory

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
        for key, value in self.link_data.items():
            self.assertEqual(getattr(link, key), value)
