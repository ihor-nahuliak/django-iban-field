from threading import local
from collections import UserString

from django_global_request.middleware import get_request
from django.contrib.auth.models import AnonymousUser


def get_user():
    """Take an access to the global user instance."""
    request = get_request()
    if not request:
        return AnonymousUser()
    return request.user


class IBANHiddenValue(UserString, str):
    _full_value = None

    def __init__(self, value):
        if value:
            value = value.replace(' ', '')
            data = '%s%s' % ('*' * (len(value) - 4), value[-4:])
            if get_user().is_superuser:
                self._full_value = self._format(value)
        else:
            data = ''
        super().__init__(data)

    @classmethod
    def _format(cls, value):
        grouping = 4
        value = value.upper().replace(' ', '').replace('-', '')
        value = ' '.join(value[i:i + grouping]
                         for i in range(0, len(value), grouping))
        return value

    @property
    def full_value(self):
        return self._full_value

    def __str__(self):
        return self._format(self.data)

    __repr__ = __str__

    def __eq__(self, other):
        # can be equal full filled values only
        return (self.full_value is not None and
                self.full_value == other.full_value)
