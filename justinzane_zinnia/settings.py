'''
justinzane_zinnia.settings
@updated: on Dec 1, 2012
@author: justin
@license:  AGPLv3
    Copyright (C) 2012  Justin Chudgar,
    5040 Saddlehorn Rd, Weed, CA 96094
    <justin@justinzane.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (('Justin Zane', 'justin@justinzane.com'),)
MANAGERS = ADMINS
SECRET_KEY = 'u$cs#oz79x($p&amp;2zt!pylo-g8tnae5*7!uvey6vo%pywo8x8yg'
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = 'justinzane_zinnia.urls'
WSGI_APPLICATION = 'justinzane_zinnia.wsgi.application'
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
#------------------------------------------------------------------------------
BITLY_LOGIN = 'justinzane'
BITLY_API_KEY = 'R_b250454a8d4f968ab43886dc14a247c0'
ZINNIA_URL_SHORTENER_BACKEND = 'zinnia.url_shortener.backends.bitly'
TWITTER_CONSUMER_KEY = 'NgLRTjEBLeVPGX61DYw'
TWITTER_CONSUMER_SECRET = 'KxEnnpd9sqmdlTgxDScnGH8NSI5ywUWHaErp8bO5E'
TWITTER_ACCESS_KEY = '21795117-bsGrqLGqC113GYIuOQej6ENDFHXt2OrDD3gg4FLrB'
TWITTER_ACCESS_SECRET = 'igtPpY5myu4bWlXMe2WQhV0TQCRVukfu6MCpFK9NoFg'
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS
#------------------------------------------------------------------------------
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django_bitly',
    'django_xmlrpc',
    'tweepy',
    'tagging',
    'mptt',
    'zinnia',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'zinnia.context_processors.version',
)
TEMPLATE_DIRS = ()
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zinnia',
        'USER': 'zinnia',
        'PASSWORD': '_F00f3b02',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
