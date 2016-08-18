# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client, RequestFactory

from link import utils, models


class UtilsTestCase(TestCase):
    def test_get_view_names(self):
        print utils.get_view_names()
