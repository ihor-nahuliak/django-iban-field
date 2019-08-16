SECRET_KEY = 'test'

INSTALLED_APPS = (
    'django_iban_field',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
