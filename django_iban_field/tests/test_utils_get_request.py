import unittest
import unittest.mock as mock

import django.test


class TestCase(django.test.TestCase):

    def setUp(self):
        super().setUp()

        m_local_patch = mock.patch('django_iban_field.utils.local')
        self.m_local_func = m_local_patch.start()
        self.addCleanup(m_local_patch.stop)

        self.m_local = self.m_local_func.return_value = mock.Mock()
        self.m_local.request = None

        from django_iban_field.utils import get_request

        self.get_request = get_request

    def test_request_is_none(self):
        self.m_local.request = None

        self.assertIsNone(self.get_request())

    def test_request_is_not_none(self):
        self.m_local.request = mock.Mock()

        self.assertIsNotNone(self.get_request())


if __name__ == '__main__':
    unittest.main()
