from localflavor.generic import models

from django_iban_field.utils import IBANHiddenValue


class IBANField(models.IBANField):
    """
    International Bank Account Number format support.
        1. The stored value is never fully visible,
           given an IBAN like "GR96 0810 0010 0000 0123 4567 890",
           the is displayed as "---7890" everywhere
        2. Superusers are able to see the full value when needed.
    """

    def from_db_value(self, value, *args, **kwargs):
        if value is None:
            return value
        return IBANHiddenValue(value)
