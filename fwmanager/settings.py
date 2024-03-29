"""
Django settings for fwmanager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ldjfpywz7oa0(h86is*2b=3bvyetp)@p0+!c%___*p^52p996i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clusters',
    'firewalls',
    'rest_framework',
    'crispy_forms',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'fwmanager.urls'

WSGI_APPLICATION = 'fwmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db/db.sqlite3'),
      #'ENGINE': 'django.db.backends.mysql',
      #'NAME': 'firewall',
      #'USER': 'fwadmin',
      #'HOST': '192.168.99.100',
      #'PASSWORD': 'redhat'
      }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Australia/Sydney'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#REST_FRAMEWORK = {
#
#	'DEFAULT_PERMISSION_CLASSES': [
#		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#	]
#}
CRISPY_TEMPLATE_PACK = 'bootstrap3'
