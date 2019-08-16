import unittest
import unittest.mock as mock

import django.test


class TestCase(django.test.TestCase):

    def setUp(self):
        super().setUp()

        m_get_request_patch = mock.patch(
            'django_iban_field.utils.get_request')
        self.m_get_request = m_get_request_patch.start()
        self.addCleanup(m_get_request_patch.stop)

        from django_iban_field.utils import get_user

        self.get_user = get_user

    def test_user_is_anonymous(self):
        self.m_get_request.return_value = None

        self.assertTrue(self.get_user().is_anonymous)

    def test_user_is_not_anonymous(self):
        self.m_get_request.return_value = mock.Mock()
        self.m_get_request.return_value.user = mock.Mock()
        self.m_get_request.return_value.user.is_anonymous = False

        self.assertFalse(self.get_user().is_anonymous)


if __name__ == '__main__':
    unittest.main()
