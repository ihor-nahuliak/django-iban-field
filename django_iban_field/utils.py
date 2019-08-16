from collections import UserString

from django.contrib.auth.models import AnonymousUser
from django_global_request.middleware import get_request


def get_user():
    """Take an access to the global user instance."""
    request = get_request()
    if not request:
        return AnonymousUser()
    return request.user


class IBANHiddenValue(UserString):
    _full_value = None

    def __init__(self, value):
        if value:
            value = value.replace(' ', '')
            data = '---%s' % value[-4:]
            if get_user().is_superuser:
                self._full_value = self._format(value)
        else:
            data = ''
        super().__init__(data)

    @classmethod
    def _format(cls, value):
        result = []
        buf = []
        for i, s in enumerate(value):
            buf.append(s)
            if (i + 1) % 4 == 0 or i == len(value) - 1:
                result.append(''.join(buf))
                buf.clear()
        return ' '.join(result)

    @property
    def full_value(self):
        return self._full_value
