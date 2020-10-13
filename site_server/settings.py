import os  # isort:skip
from os.path import normpath, join

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

"""
Django settings for pages project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

ENV = "DEVELOPMENT"
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    LOG_DIR = "/var/log/" + ENV
except:
    LOG_DIR = "/var/log/" + ENV

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'orphwaiuvhawif237r23uhfp9qe7gfte8ft9p7fqe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.3', '10.42.0.1', '10.42.0.122']

# Application definition
ROOT_URLCONF = 'site_server.urls'
WSGI_APPLICATION = 'site_server.wsgi.application'

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Johannesburg'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'site_server', 'static'),
)
SITE_ID = 1
SITE_NAME = 'localhost'
SITE_URL = 'http://127.0.0.1'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'site_server', 'templates'),
            os.path.join(BASE_DIR, 'site_server', 'templates', 'allauth')
        ],
        'OPTIONS': {
            'context_processors': [

                # `allauth` needs this from django
                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'

            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    # make the admin section sparkle
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',

    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    # Main application
    'site_server',
    'django.contrib.sites',

    # Authentication modules from social media platforms
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',

    # Easy to get lost in the applications
    # But each of these give more functionality
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'mptt',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',

    # App hooks
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'djangocms_blog',
    'rest_framework',
    'rest_framework.authtoken',
    # Custom API
    'api',
    'shell_plus',
    'favicon',
    # Start of invoicing module
    'widget_tweaks',

]

LANGUAGES = (
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'hide_untranslated': False,
            'public': True,
            'redirect_on_fallback': True,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

# Default template used
CMS_TEMPLATES = (
    ('climate/home.html', 'Climate'),
)

X_FRAME_OPTIONS = '*'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': gettext('Content'),
        'plugins': ['TextPlugin', 'LinkPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': '<p>Great websites : %(_tag_child_1)s and %(_tag_child_2)s</p>'
                },
                'children': [
                    {
                        'plugin_type': 'LinkPlugin',
                        'values': {
                            'name': 'django',
                            'url': 'https://www.djangoproject.com/'
                        },
                    },
                    {
                        'plugin_type': 'LinkPlugin',
                        'values': {
                            'name': 'django-cms',
                            'url': 'https://www.django-cms.org'
                        },
                    },
                ]
            },
        ]
    }
}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
    ],
    'skin': 'moono-lisa',
}

DATABASE_NAME = 'project.db'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': DATABASE_NAME,
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True

BLOG_AVAILABLE_PERMALINK_STYLES = (
    ('slug', gettext('Slug')),
    ('full_date', gettext('Full date')),
    ('short_date', gettext('Year /  Month')),
    ('category', gettext('Category')),

)

BLOG_PERMALINK_URLS = {
    'full_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-˓→\w]*)/$',
    'short_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>\w[-\w]*)/$',
    'category': r'^(?P<category>\w[-\w]*)/(?P<slug>\w[-\w]*)/$',
    'slug': r'^(?P<slug>\w[-\w]*)/$',
}

# PARLER_LANGUAGES = {1: (
#     {'code': 'en', },
#     {'code': 'it', },
#     {'code': 'fr', },
# ), 'default': {'fallbacks': ['en', 'it', 'fr'], }
# }

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# MEDIA_ROOT = os.environ.get('FILER_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
#
#
# MEDIA_URL = '/prod/STAGING/RyleeMonster/media/'

FILER_CANONICAL_URL = 'sharing/'

FAVICON_PATH = MEDIA_URL + 'favicon.ico'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_GB',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.5',
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    },
    'linkedin': {
        'HEADERS': {
            'x-li-src': 'msdk'
        },
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ],
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    }
}

LOGIN_REDIRECT_URL = "/?social_login=true"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = '/accounts/social_login/'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # a personal preference. True by default. I don't want users to be interrupted by logging in
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # a personal preference. I don't want to add 'i don't remember my username' like they did at Nintendo, it's stupid
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'myapp:email_success'  # a page to identify that email is confirmed
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7  # a personal preference. 3 by default
ACCOUNT_EMAIL_REQUIRED = True  # no questions here
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # as the email will be used for login
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True  # False by default
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True  # True by default
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_USERNAME_BLACKLIST = ['suka', 'blyat', ]  # :D
ACCOUNT_USERNAME_MIN_LENGTH = 4  # a personal preference
ACCOUNT_SESSION_REMEMBER = True  # None by default (to ask 'Remember me?'). I want the user to be always logged in
SOCIALACCOUNT_AVATAR_SUPPORT = True
LOGIN_ON_EMAIL_CONFIRMATION = True

import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        # 'special': {
        #     '()': 'django.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(LOG_DIR, 'INFO.log'),
        },
        'console_debug_false': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(LOG_DIR, 'ERROR.log'),
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(LOG_DIR, 'SERVER.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(LOG_DIR, 'MAIL.log'),
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(LOG_DIR, 'DEBUG.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_debug_false', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

logging.config.dictConfig(LOGGING)

l1 = logging.getLogger()
l2 = logging.getLogger('')
root = logging.root

l1.info("l1")
l2.info("l2")
root.info("root logger")

EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

BLOG_AUTO_HOME_TITLE = "Weather Watch"
BLOG_AUTO_BLOG_TITLE = "Weather Watch Blog"
BLOG_AUTO_APP_TITLE = "Weather Watch Application"
BLOG_AUTO_NAMESPACE = "weather-watch-application"

BLOG_POSTS_LIST_TRUNCWORDS_COUNT = 20