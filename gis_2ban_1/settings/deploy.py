from .base import *
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy


# 이 부분이 base.py 파일이랑 중복으로 들어가있네요
# BASE_DIR = Path(__file__).resolve().parent.parent
def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}