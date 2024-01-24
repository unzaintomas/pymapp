from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbpym',
<<<<<<< HEAD
        'USER': 'postgres',#'pymapp',
=======
        'USER': 'pymapp',
>>>>>>> 5b85c461a413f0019ff6dcce6b60f44c8b8e5b10
        'PASSWORD': 'masterkey',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
