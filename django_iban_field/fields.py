from django.db import models
from django.utils.translation import gettext_lazy as _

from django_iban_field.utils import get_user


class IBANField(models.CharField):
    default_validators = []
    description = _('International Bank Account Number')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 34)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if not get_user().is_superuser:
            value = '---%s' % value.replace(' ', '')[-4:]
        return value
