"""
Django settings for RestFilm project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .settings_secret import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gettext = lambda s: s

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'Movies',
    'tinymce',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'viktorkozachok21@gmail.com'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RestFilm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'RestFilm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'db.sqlite3',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


TINYMCE_DEFAULT_CONFIG = {
'height': 360,
'width': 1120,
'cleanup_on_startup': True,
'custom_undo_redo_levels': 20,
'selector': 'textarea',
'theme': 'modern',
'plugins': '''
    textcolor save link image media preview codesample contextmenu
    table code lists fullscreen insertdatetime nonbreaking
    contextmenu directionality searchreplace wordcount visualblocks
    visualchars code fullscreen autolink lists charmap print hr
    anchor pagebreak
    ''',
'toolbar1': '''
    fullscreen preview bold italic underline | fontselect,
    fontsizeselect | forecolor backcolor | alignleft alignright |
    aligncenter alignjustify | indent outdent | bullist numlist table |
    | link image media | codesample |
    ''',
'toolbar2': '''
    visualblocks visualchars |
    charmap hr pagebreak nonbreaking anchor | code |
    ''',
'contextmenu': 'formats | link image',
'menubar': True,
'statusbar': True,
}

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('uk', gettext(u'Укр')),
    ('en', gettext(u'Анг')),
)

LANGUAGES_LOCALES = {
    'uk': 'uk_UA.UTF-8',
    'en': 'en_US.UTF-8',
}

LOCALE_PATHS = (os.path.join(os.path.dirname(BASE_DIR), 'locale'),)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TINYMCE_COMPRESSOR = False

TINYMCE_FILEBROWSER = True

TINYMCE_SPELLCHECKER = True

FILEBROWSER_DIRECTORY = ''

DIRECTORY = ''

FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.pdf', '.tiff'],
    'Document': ['.doc', '.docx', '.rtf', '.txt', '.xls', '.xslx', '.csv', '.ppt', '.pptx'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p'],
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), 'assets')
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROBOTS_USE_SITEMAP = False

ROBOTS_SITEMAP_URLS = [
    'http://localhost:8000/sitemap.xml',
]

ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'

ROBOTS_USE_HOST = False

ROBOTS_USE_SCHEME_IN_HOST = True

SITE_ID = 1
