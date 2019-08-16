from django.conf import settings
from django.db import models

from django_iban_field.fields import IBANField


if settings.TESTING:
    # It needs just to test the field.

    class TestModel(models.Model):
        iban = IBANField(null=True, db_index=True)

        class Meta:
            app_label = 'django_iban_field'
