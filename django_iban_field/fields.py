from localflavor.generic import models

from django_iban_field.utils import IBANHiddenValue


class IBANFieldDescriptor:
    def __init__(self, field):
        self.name = field.name
        self.hidden_name = '_%s' % field.name

    def __set__(self, instance, value):
        if value is not None and len(value) > 4 and not value.startswith('-'):
            instance.__dict__[self.name] = '---%s' % value[-4:]
            instance.__dict__[self.hidden_name] = value
        else:
            instance.__dict__[self.name] = None
            instance.__dict__[self.hidden_name] = None

    def __get__(self, instance, owner=None):
        if instance is not None and self.hidden_name in instance.__dict__:
            value = instance.__dict__[self.hidden_name]
            return value
        return None


class IBANField(models.IBANField):
    """
    International Bank Account Number format support.
        1. The stored value is never fully visible,
           given an IBAN like "GR96 0810 0010 0000 0123 4567 890",
           the is displayed as "---7890" everywhere
        2. Superusers are able to see the full value when needed.
    """
    hidden_field = None
    concrete = False

    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls, name, private_only=private_only)
        self.hidden_field = self.clone()
        self.hidden_field.name = '_%s' % self.name
        self.hidden_field.attname = '_%s' % self.attname
        self.hidden_field.column = '_%s' % self.column
        self.hidden_field.hidden = True
        cls._meta.add_field(self.hidden_field, private=True)
        setattr(cls, name, IBANFieldDescriptor(self))
