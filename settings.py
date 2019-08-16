import os


SECRET_KEY = 'test'
TESTING = True

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

FIXTURE_DIRS = (
   os.path.join(ROOT_PATH, 'django_iban_field', 'tests', 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_global_request',
    'localflavor',
    'django_iban_field',
)

MIDDLEWARE = (
    'django_global_request.middleware.GlobalRequestMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
