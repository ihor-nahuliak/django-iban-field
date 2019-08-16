from threading import local

from django.contrib.auth.models import AnonymousUser


def get_request():
    """Take an access to the global request instance."""
    return getattr(local(), 'request', None)


def get_user():
    """Take an access to the global user instance."""
    request = get_request()
    if not request:
        return AnonymousUser()
    return request.user
