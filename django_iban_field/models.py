from django.conf import settings
from django.db import models

from django_iban_field.fields import IBANField


class TestModel(models.Model):
    iban = IBANField(null=True, db_index=True)

    class Meta:
        app_label = 'django_iban_field'
