"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!k3ozd9m%eq!7!yu@7s0i8a-r0jpx^g3&f)2dsp-fj2ebew4s2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'web.apps.WebConfig',
    'products.apps.ProductsConfig',
    'newsletters.apps.NewslettersConfig',
    'articles.apps.ArticlesConfig',
    'taggit',
    'taggit_helpers',
    'analytical',
    'crispy_forms',
    'django_summernote',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'cms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

GRAPPELLI_ADMIN_TITLE = 'CMS Contacto.top'

GRAPPELLI_AUTOCOMPLETE_LIMIT = 10

GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = 10

GRAPPELLI_SWITCH_USER = False

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ANALYTICAL_AUTO_IDENTIFY = True

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-86275612-1'

GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = True

GOOGLE_ANALYTICS_SITE_SPEED = True

GOOGLE_ANALYTICS_SESSION_COOKIE_TIMEOUT = 3600000

GOOGLE_ANALYTICS_VISITOR_COOKIE_TIMEOUT = 3600000

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '100%',
    'height': '500',

    # Or, set editor language/locale forcely
    'lang': 'es-ES',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'superscript', 'subscript', 'strikethrough', 'clear']],
        ['para', ['ul', 'ol', 'height']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video', 'hr']],
    ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # Codemirror as codeview
    'codemirror': {
        # Please visit http://summernote.org/examples/#codemirror-as-codeview
        'theme': 'monokai',
    },

}

if DEBUG:
    def show_toolbar(request):
        return True


    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
