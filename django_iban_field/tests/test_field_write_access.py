import unittest
import unittest.mock as mock

import django.test
from django.core.management import call_command


class TestCase(django.test.TestCase):

    def setUp(self):
        super().setUp()
        call_command('loaddata', 'initial_data.json', verbosity=0)

        m_get_user_patch = mock.patch('django_iban_field.utils.get_user')
        self.m_get_user = m_get_user_patch.start()
        self.addCleanup(m_get_user_patch.stop)

        self.m_user = self.m_get_user.return_value = mock.Mock()
        self.m_user.is_superuser = False

        from django_iban_field.models import TestModel

        self.TestModel = TestModel

    def test_not_admin_user_update_none_value(self):
        self.m_user.is_superuser = False
        self.TestModel.objects.filter(id=2).update(iban=None)
        m = self.TestModel.objects.get(id=2)

        self.assertIsNone(m.iban)

    def test_not_admin_user_save_none_value(self):
        self.m_user.is_superuser = False
        m = self.TestModel.objects.get(id=2)
        m.iban = None
        m.save()

        self.assertIsNone(m.iban)

    def test_not_admin_user_update_value(self):
        self.m_user.is_superuser = False
        self.TestModel.objects.filter(id=1).update(
            iban='GR96 0810 0010 0000 0123 4567 890')
        m = self.TestModel.objects.get(id=1)

        self.assertEqual('---7890', m.iban)
        self.assertIsNone(m.iban.full_value)

    def test_not_admin_user_save_value(self):
        self.m_user.is_superuser = False
        m = self.TestModel.objects.get(id=1)
        m.iban = 'GR96 0810 0010 0000 0123 4567 890'
        m.save()

        self.assertEqual('---7890', m.iban)
        self.assertIsNone(m.iban.full_value)

    def test_admin_user_update_none_value(self):
        self.m_user.is_superuser = True
        self.TestModel.objects.filter(id=2).update(iban=None)
        m = self.TestModel.objects.get(id=2)

        self.assertIsNone(m.iban)

    def test_admin_user_update_value(self):
        self.m_user.is_superuser = True
        self.TestModel.objects.filter(id=1).update(
            iban='GR96 0810 0010 0000 0123 4567 890')
        m = self.TestModel.objects.get(id=1)

        self.assertEqual('---7890', m.iban)
        self.assertEqual('GR96 0810 0010 0000 0123 4567 890',
                         m.iban.full_value)


if __name__ == '__main__':
    unittest.main()
