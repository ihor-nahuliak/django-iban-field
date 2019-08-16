import unittest
import unittest.mock as mock

import django.test


class TestCase(django.test.TestCase):

    def setUp(self):
        super().setUp()

        m_get_user_patch = mock.patch('django_iban_field.fields.get_user')
        self.m_get_user = m_get_user_patch.start()
        self.addCleanup(m_get_user_patch.stop)

        self.m_user = self.m_get_user.return_value = mock.Mock()
        self.m_user.is_superuser = False

        from django_iban_field.models import TestModel

        self.TestModel = TestModel
        self.TestModel.objects.create(
            id=1, iban=None)
        self.TestModel.objects.create(
            id=2, iban='GR96 0810 0010 0000 0123 4567 890')

    def test_not_admin_user_see_none_value(self):
        self.m_user.is_superuser = False
        m = self.TestModel.objects.get(id=1)

        self.assertIsNone(m.iban)

    def test_not_admin_user_see_the_hidden_string(self):
        self.m_user.is_superuser = False
        m = self.TestModel.objects.get(id=2)

        self.assertEqual('---7890', m.iban)

    def test_admin_user_see_none_value(self):
        self.m_user.is_superuser = True
        m = self.TestModel.objects.get(id=1)

        self.assertIsNone(m.iban)

    def test_admin_user_see_the_full_string(self):
        self.m_user.is_superuser = True
        m = self.TestModel.objects.get(id=2)

        self.assertEqual('GR96 0810 0010 0000 0123 4567 890', m.iban)


if __name__ == '__main__':
    unittest.main()
