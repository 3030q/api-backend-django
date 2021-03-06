from django.test import TestCase
from parser_project import models


class YourTestClass(TestCase):

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)


class WebsiteTests(TestCase):

    def test_page_is_created_successfully(self):
        page = models.Page(
            name='Home',
            slug='home'
        )
        page.save()
