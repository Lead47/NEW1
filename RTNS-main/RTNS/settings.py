"""
Django settings for RTNS project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c5zxqfl__lurt72o+$i!fcta+r8#m(mff3169*53qy(+xt@o-#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_social_share',
    'core',
    'user_auth',
    'article',
    'events',
    'speakers',
    'committee',
    'django_extensions',
    'contact_us',
    'channels',
    'crispy_forms',
    'certificate',
    'event_reg',
    'partials'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RTNS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.header_context',
                'utils.context_processors.footer_context',
                'utils.context_processors.dep_logo',
                'utils.context_processors.sponsor_logo',
            ],
        },
    },
]

WSGI_APPLICATION = 'RTNS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER':'postgres',
        'PASSWORD':'eLrNLvOofALrBiFXUqBdhLikxOZzCZpE',
        'HOST': 'centerbeam.proxy.rlwy.net',
        'PORT': '15037', 
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATICSTORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    'site_header':"RTNS",
    'site_brand':"RTNS",
    'site_logo':"Image/RTNSlogobg.png",
    'copyright': "RTNS@copyright",
}

AUTH_USER_MODEL= "user_auth.User"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'hussainnawazkb5500@gmail.com'
EMAIL_HOST_PASSWORD = 'HA678954'

ADMIN_EMAIL='adeebhassi@gmail.com'
# settings.py
ALLOWED_HOSTS = ['rtns-uejbd.org','web-production-83bf.up.railway.app',]
#ALLOWED_HOSTS = ["*"]
LOGIN_URL = 'user_auth:user_signin'

GOOGLE_DRIVE_CREDENTIALS = os.path.join(BASE_DIR, 'rtns-413207-168420d2b7cd.json')
CSRF_TRUSTED_ORIGINS=['https://web-production-83bf.up.railway.app','https://rtns-uejbd.org']