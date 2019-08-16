import unittest
import unittest.mock as mock

import django.test


class TestCase(django.test.TestCase):

    def setUp(self):
        super().setUp()

        m_get_user_patch = mock.patch('django_iban_field.utils.get_user')
        self.m_get_user = m_get_user_patch.start()
        self.addCleanup(m_get_user_patch.stop)

        self.m_user = self.m_get_user.return_value = mock.Mock()
        self.m_user.is_superuser = False

        from django_iban_field.utils import IBANHiddenValue

        self.IBANHiddenValue = IBANHiddenValue

    def test_not_admin_user_see_empty_value(self):
        self.m_user.is_superuser = False
        value = self.IBANHiddenValue(None)

        self.assertEqual('', value)
        self.assertIsNone(value.full_value)

    def test_not_admin_user_see_the_hidden_string(self):
        self.m_user.is_superuser = False
        value = self.IBANHiddenValue('GR96 0810 0010 0000 0123 4567 890')

        self.assertEqual('---7890', value)
        self.assertIsNone(value.full_value)

    def test_admin_user_see_empty_value(self):
        self.m_user.is_superuser = True
        value = self.IBANHiddenValue(None)

        self.assertEqual('', value)
        self.assertIsNone(value.full_value)

    def test_admin_user_see_the_full_string(self):
        self.m_user.is_superuser = True
        value = self.IBANHiddenValue('GR96 0810 0010 0000 0123 4567 890')

        self.assertEqual('---7890', value)
        self.assertEqual('GR96 0810 0010 0000 0123 4567 890', value.full_value)

    def test_format_austria_iban(self):
        self.m_user.is_superuser = True
        value = self.IBANHiddenValue('AT611904300234573201')

        self.assertEqual('---3201', value)
        self.assertEqual('AT61 1904 3002 3457 3201', value.full_value)

    def test_format_germany_iban(self):
        self.m_user.is_superuser = True
        value = self.IBANHiddenValue('DE89370400440532013000')

        self.assertEqual('---3000', value)
        self.assertEqual('DE89 3704 0044 0532 0130 00', value.full_value)

    def test_format_spanish_iban(self):
        self.m_user.is_superuser = True
        value = self.IBANHiddenValue('ES9121000418450200051332')

        self.assertEqual('---1332', value)
        self.assertEqual('ES91 2100 0418 4502 0005 1332', value.full_value)


if __name__ == '__main__':
    unittest.main()
