"""
Django settings for AWS3R project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_%tlzo-kj37uor$*gn^fe%9u=i2z0)7&y-zp-qqe98h%^-=ni$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'educate',
    # 'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware,'
    
]

ROOT_URLCONF = 'AWS3R.urls'

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

WSGI_APPLICATION = 'AWS3R.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddac_backend',
        'USER': 'DDAC061320',
        'PASSWORD': 'Nice10day',
        'HOST': 'ddacbackend2.cd8eu2k4w9p7.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Update AWS_KEY_ID, SECRET_ACCESS_KEY and SESSION_TOKEN fields everytime 
AWS_ACCESS_KEY_ID = 'ASIAQ3EGU5RWIHDZZTZO'
AWS_SECRET_ACCESS_KEY = 'o+x8T01OiRnv52Tx4FmdLkcsXALhjnW4XL4qRWR+'
AWS_SESSION_TOKEN='IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC7NW3nxPzaJAY39cAz/zbJ2ysNCDyGQ1EGzE3PY3WBPQIhAPrgQvRZrcbDPX6D6Guqb6TBIW3kvycLm2dKMg6RpPvbKrsCCIn//////////wEQABoMMDU4MjY0NDQ4MTA4Igx6l3SmOLfVCcuf2P8qjwIBflTMYgS0xMg99X0U3s/nL6N2acXwq8euZf7WKSH+XXGhRHVGBzP2+YQnZXzrn5cAA/q9H7WTPxeXJ6qJYW3H+jgZBZ5gzMGlCYE6giuqFGSFbxBuxZPDXNCbYsxN0tb9QCicnFX4r1jJMOmQUrhdufd9Lg/J0tHV7S7d6IoyWv8xJdpiNZc3MYvzHwD7eGdNS4Gky/korl+l2z1IKSh9ls7J+s1qMAge2bU4z4ILJa02P40c0kf4m82PoxEz1pIbrhEtOylbD5WSY7GfN75jaI77iPnuIKC+n5o5RUyEzEO90Mx8Tp3e7veJExsdXksCISeibdo1deofUytyesWTxMd7HmKOHoTePNhvvzzDMOiN7rAGOpwB7Rmg9CRhQfbDoaC/SkX21D6IvKt1PHx4Ksey2AFH0xOJ4caeVdnv7T/J0FJhhyCYcdXAEz9DRRZekn4nhUtH2n+ev5uwRg0VIb8fhp/xVI9AZU4O9/bCpNmb44gNhVaK1tnU+dQfHrAxrzqS5+Et/kE4YbUu/yBheZmhLtl3R6IZ3ldn3s8biSR7cFEXmWc+2MMZfvFYY8yeoNED'
AWS_STORAGE_BUCKET_NAME = 'ddacs3'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

