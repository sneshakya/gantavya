"""
Django settings for gantavya project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import environ
from pathlib import Path

from django.conf.global_settings import STATICFILES_DIRS


env = environ.Env(
	# set casting, default value
	DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path( __file__ ).resolve().parent.parent

environ.Env.read_env( os.path.join( BASE_DIR, ".env" ) )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ('django-insecure-4x*ks%6l_@n3oa#%zc_*l+39v!2@%^#5fs0po2k5o44!2'
              '-44ni')
# Google OAuth ->
OAUTH_CLIENT_ID = env( "OAUTH_CLIENT_ID" )
OAUTH_SECRET_KEY = env( "OAUTH_SECRET_KEY" )

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
	"google": {
		"APPS": [
			{
				"client_id": OAUTH_CLIENT_ID,
				"secret": OAUTH_SECRET_KEY,
				"key": "",
				"settings": {
					"scope": [
						"profile",
						"email",
					],
					"auth_params": {
						"access_type": "online",
					},
				},
			},
		],
	}
}
# <- Google OAuth

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]

APPEND_SASH = True
AUTH_USER_MODEL = "accounts.CustomUser"

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',

	'rest_framework',
	'django_browser_reload',
	'fontawesomefree',

	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.google',

	'accounts',
	'trips'
]

MIDDLEWARE = [
	'allauth.account.middleware.AccountMiddleware',

	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

	"django_browser_reload.middleware.BrowserReloadMiddleware",
]

AUTHENTICATION_BACKENDS = [
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'gantavya.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			'gantavya/templates',
		],
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

WSGI_APPLICATION = 'gantavya.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.mysql",
		"OPTIONS": {
			"read_default_file": "my.cnf",
		},
	}
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation'
		        '.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation'
		        '.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation'
		        '.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation'
		        '.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'staticfiles/'
STATICFILES_DIRS = [
	BASE_DIR / "staticfiles",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	]
}
