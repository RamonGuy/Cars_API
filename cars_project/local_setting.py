# SECURITY WARNING: keep the secret key used in production secret!
from pickle import TRUE


SECRET_KEY = 'django-insecure-fnqnj%rb5yej%2_4!%trz=eeu@qg5zk7gwu-n_%=i-$^$8b)fa'
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'USER': 'root',
        'PASSWORD': 'Shadow2fly4u',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
