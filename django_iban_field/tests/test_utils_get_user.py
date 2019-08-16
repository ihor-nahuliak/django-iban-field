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

        from django_iban_field.utils import get_user

        self.get_user = get_user

    def test_user_is_anonymous(self):
        self.m_local.request = None

        self.assertTrue(self.get_user().is_anonymous)

    def test_user_is_not_anonymous(self):
        self.m_local.request = mock.Mock()
        self.m_local.request.user = mock.Mock()
        self.m_local.request.user.is_anonymous = False

        self.assertFalse(self.get_user().is_anonymous)


if __name__ == '__main__':
    unittest.main()
