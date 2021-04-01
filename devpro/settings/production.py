from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bev9ycfrbmrovoadpooc',
        'USER':'uyikd1tl92incu9b',
        'PASSWORD':'t9kMr8fv2NG1EfroSfPC',
        'HOST':'bev9ycfrbmrovoadpooc-mysql.services.clever-cloud.com'
    }
}
