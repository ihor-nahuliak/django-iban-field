from collections import UserString

from django.contrib.auth.models import AnonymousUser
from django_global_request.middleware import get_request


def get_user():
    """Take an access to the global user instance."""
    request = get_request()
    if not request:
        return AnonymousUser()
    return request.user


class IBANHiddenValue(UserString, str):
    """The class that implements access to the full viewed IBAN value.
    For non superuser users it's shown just cut IBAN version.

    >>> iban = IBANHiddenValue('GR96 0810 0010 0000 0123 4567 890')
    >>> iban.full_value  # user.is_superuser is True
    'GR96 0810 0010 0000 0123 4567 890'
    >>> iban.full_value  # user.is_superuser is False
    None
    >>> iban
    ---7890
    """
    _full_value = None

    def __init__(self, value):
        if isinstance(value, self.__class__):
            value = value.full_value
        super().__init__(value)
        if value:
            value = value.replace(' ', '')
            self.data = '---%s' % value[-4:]
            if get_user().is_superuser:
                self._full_value = self._format(value)

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
