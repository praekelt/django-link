from django.test import TestCase

from link import utils


class UtilsTestCase(TestCase):
    def test_get_view_names(self):
        self.assertEqual(
            utils.get_view_names(),
            ["link-1", "link-2", "link:link-list", "link:link-detail"]
        )
