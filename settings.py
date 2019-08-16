import os


SECRET_KEY = 'test'
DEBUG = TESTING = True

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

FIXTURE_DIRS = (
   os.path.join(ROOT_PATH, 'django_iban_field', 'tests', 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_global_request',
    'localflavor',
    'django_iban_field',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.db.sqlite3',
    }
}

REQUIREMENTS_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_global_request.middleware.GlobalRequestMiddleware',
]

PROJECT_MIDDLEWARE = [
]

MIDDLEWARE = REQUIREMENTS_MIDDLEWARE + PROJECT_MIDDLEWARE

STATIC_URL = '/static/'
ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
