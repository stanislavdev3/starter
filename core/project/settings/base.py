import os

import environ

# ======================= BASE ===============================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# ======================= ENV ================================================
env = environ.Env(
    DEBUG=(bool, False),
    APP_INSTANCE=(str, 'prod'),
)

if os.path.isfile(os.path.join(BASE_DIR, 'project', 'settings', '.env')):
    environ.Env.read_env(os.path.join(BASE_DIR, 'project', 'settings', '.env'))

DEBUG = env('DEBUG')
APP_INSTANCE = env('APP_INSTANCE')

# ======================= SECURITY ===========================================
ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY', default='y$o97r*90ixip94186+%_7&2o018hlyvd8n3hzecf6gyirnd4r')

# ======================= APPLICATIONS =======================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ======================= MIDDLEWARE =========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ======================= URLS ===============================================
ROOT_URLCONF = 'project.urls'

# ======================= TEMPLATES ==========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# ======================= USGI ===============================================
WSGI_APPLICATION = 'project.wsgi.application'

# ======================= DATABASES ==========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB', default='market'),
        'USER': env('POSTGRES_USER', default='root'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='root'),
        'HOST': env('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': env('POSTGRES_PORT', default=5432),
    },
}

# ======================= LOCALE =============================================
LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ======================= STATIC =============================================
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# ======================= MEDIA =============================================
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# ======================= SENTRY =========================================
SENTRY_URL = 'https://sentry.io/api/embed/error-page/'

# ======================= LOGGING ================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'propagate': False,
        },
    }
}
