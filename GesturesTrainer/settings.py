"""
Django settings for GesturesTrainer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6s5*m5a&+a524)#wr2+0ua&-(56!2uy#*rm82n3hojbods(s-n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'exercises',
    'djfrontend',
    'djfrontend.skeleton',
    'import_export',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'GesturesTrainer.middlewares.ForceDefaultLanguageMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',



)

ALLOWED_HOSTS = [
    '.wingcheecuhk.me', # Allow domain and subdomains
    '.wingcheecuhk.me.', # Also allow FQDN and subdomains
    'localhost', 
    '127.0.0.1',
]

SOCIAL_AUTH_FACEBOOK_KEY = '693217374157462'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c27cee84b8c849c075046743a74ce937'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}



# LOGIN_URL          = '/login-form/'
# LOGIN_REDIRECT_URL = '/logged-in/'
# LOGIN_ERROR_URL    = '/login-error/'

# SOCIAL_AUTH_USER_MODEL = 'profiles.User'

# only for mysql backend to enforce field length, some oauth ppl use longer retarded keys
SOCIAL_AUTH_UID_LENGTH = 223

SOCIAL_AUTH_DEFAULT_USERNAME = 'user'

# only needed if email is username
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = False

# for security
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

# These URLs are used on different steps of the auth process, some for successful results and others for error situations.

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard'
# Used to redirect the user once the auth process ended successfully. The value of ?next=/foo is used if it was present
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/'
# URL where the user will be redirected in case of an error
SOCIAL_AUTH_LOGIN_URL = '/dashboard'
# Is used as a fallback for LOGIN_ERROR_URL
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/dashboard'
# Used to redirect new registered users, will be used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL if defined. Note that ?next=/foo is appended if present
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/dashboard'
# Like SOCIAL_AUTH_NEW_USER_REDIRECT_URL but for new associated accounts (user is already logged in). Used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/dashboard'
# The user will be redirected to this URL when a social account is disconnected
SOCIAL_AUTH_INACTIVE_USER_URL = '/dashboard'
# Inactive users can be redirected to this URL when trying to authenticate.


# disable new user creation through fb
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details', 
    'social.pipeline.social_auth.social_uid',      
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
 )


# social oauth methods
AUTHENTICATION_BACKENDS = (
    # 'social.backends.open_id.OpenIdAuth',
    # 'social.backends.google.GoogleOpenId',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    # 'social.backends.twitter.TwitterOAuth',
    # 'social.backends.yahoo.YahooOpenId',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',

)


SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

ROOT_URLCONF = 'GesturesTrainer.urls'

WSGI_APPLICATION = 'GesturesTrainer.wsgi.application'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# 30 mins cookies, turned off because it kicks user out automatically after 30 mins
# SESSION_COOKIE_AGE = 60 * 30
# SESSION_SAVE_EVERY_REQUEST = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GestureLearningDB',
        'USER': 'sa',
        'PASSWORD': 'p0o9i8u7',
        'HOST': 'gesturelearningdb.c2m7xlffp3xl.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Hongkong'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    
    # ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'GesturesTrainer/locale'),
    os.path.join(BASE_DIR, 'exercises/locale'),
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL='/media/'

# change to True if pushing to production
remoteHost = True
if remoteHost:
    
    STATIC_ROOT = "/home/ubuntu/GesturesTrainer.com/GesturesTrainer/static/"
    MEDIA_ROOT='/home/ubuntu/GesturesTrainer.com/GesturesTrainer/media/'
else:

    # used to store images of profiles
    MEDIA_ROOT='/Users/ahau/GesturesTrainer/media/'

    


