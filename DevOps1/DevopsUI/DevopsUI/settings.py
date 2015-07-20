"""
Django settings for DevopsUI project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1-dbq0v#(%5f1v*xg14v=x5yr=-us8s9o_6zru=iv565jtw7&('

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#TEMPLATE_DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/home/tcs/DevopsUI.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'DevopsUI': {
            'handlers': ['logfile'],
            'level': 'WARNING', # Or maybe INFO or DEBUG
            'propagate': False
        },
    },
}





DEBUG = True
TEMPLATE_DEBUG = DEBUG



TEMPLATE_DIRS= (
     '/home/tcs/DEVOPS-MIGRATION/DevopsUI/DevopsUI/templates',
)

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DevopsUI.urls'

WSGI_APPLICATION = 'DevopsUI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATICFILES_FINDERS = [
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#]



STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
#)

#STATIC_ROOT = ''
#STATIC_URL = BASE_DIR+'/DevopsUI/static/'

STATICFILES_DIRS = (
    # ...
    ("/home/tcs/DEVOPS-MIGRATION/DevopsUI/DevopsUI/static/"),
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.core.context_processors.static',
#)

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#    '/home/tcs/raviteja/DevopsUI/DevopsUI/static/',
#)
