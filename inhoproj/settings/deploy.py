import os, environ

from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file= os.path.join(BASE_DIR,'.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASE = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangodb',
#         'USER': 'django',
#         'PASSWORD': 'tlsdlsgh!11',
#         'HOST': 'mariadb',
#         'PORT': '3306',
#     }
# }