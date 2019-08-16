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
    'localflavor',
    'django_iban_field',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
