import unittest

import django.test
from django.conf import settings
from django.apps import apps


class TestCase(django.test.TestCase):

    def test_app_is_installed(self):
        self.assertIn('django_iban_field', settings.INSTALLED_APPS)

    def test_app_config(self):
        app = apps.get_app_config('django_iban_field')

        self.assertEqual('django_iban_field', app.label)


if __name__ == '__main__':
    unittest.main()
