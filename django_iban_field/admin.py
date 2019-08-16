from django.contrib import admin

from django_iban_field.models import TestModel


admin.site.register(TestModel, admin.ModelAdmin)
