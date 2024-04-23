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
AWS_ACCESS_KEY_ID = 'ASIAQ3EGU5RWCVRR5VGO'
AWS_SECRET_ACCESS_KEY = 'bUiCO6oOJnJtqCBFoEK2EHbVGACcdHn0TJZ9nmaS'
AWS_SESSION_TOKEN='IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIBWIMU0D6LmITgPTMJJWoAUIG2bQc8M7IXMV7c1S4hlfAiAjBiung46I3XOONjCTZpp7wTP3weYknaS+q0xN+7KUpiqyAghxEAAaDDA1ODI2NDQ0ODEwOCIM4lghoZxwf6GaDQ5jKo8C0zLNgDL8VYqPpdi0PEUrqrd1qHDb6JcrY4Xn6N8NZ+1GjSiMn8gzbDEojUNIjmgwKmYvmzS02GlpzHyiRCco5gczIsGApZ59NZI4FQeh2dF6qPj7XTFxZzq8KVoGDhsxpAB0fakZVrV0JHh/KcMkQ/8lciiS1IBIYPYAtcJWpMFgPyYE8insu9mkmNr6m2k2AKFqh+LofWgugYzMy8Udor8MSvzyYxOLGSuJ9dh950/eQobMGuGS8m40LDHg3SAAHY+osfSM1jFb4S81fAE8ciLoRc3H2QPXxOJxsNgmYbttZxDQP1682Fl2tBqvFT3jtFT5SqYfYztkV0AXGi9s7HwN+ejiLOPEoZJNuGKAaTDGz52xBjqeAfGPO4YxIPu8Y6DOGx7vEAfp5RtTmWY68V+flv2SbjaGxwpeNSoXTlqMsppEt8RzpwKnuR7Eb0GPng3q2YgNrjRtC+jyE+ROU6ACC1OnKcB5XuK+g6H5ABl2kTmL37A4OVr4anJQDtXuWVJT3NV93KQ1T554vjuTZzb3i7uishPCj3Zk5f7BlDLaxCeiawhYBTgVwCImgFGozv8hG6Es'
AWS_STORAGE_BUCKET_NAME = 'ddacs3'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

