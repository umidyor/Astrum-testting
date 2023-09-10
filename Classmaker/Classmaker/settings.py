"""
Django settings for Classmaker project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e$bcb1%s8t@%)(*_k6x!yw&hw_taam1+47-@&d&1-xeknr$2sc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestingSystem',
    'UserResponse',
    'UserResponseMatchingAndRewarding',
    'AssignLinks',
    'ckeditor',
    'ckeditor_uploader',
    'bootstrap4',
    'bootstrap_datepicker_plus',
]



CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'allowedContent':True,
        'autoParagraph':False,
        'height': 100,
        'width': 600,
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       ]},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'SpecialChar']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'yourcustomtools', 'items': [
                'Preview',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            'autolink',
            'autoembed',
            'embedsemantic',
            'widget',
            'lineutils',
            'clipboard',
            'dialogui',
            'elementspath'
        ]),
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Classmaker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Classmaker/templates')],
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

WSGI_APPLICATION = 'Classmaker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BOOTSTRAP_DATEPICKER_PLUS = {
    # Options for all input widgets
    # More options: https://getdatepicker.com/4/Options/
    "options": {
        "showClose": True,
        "showClear": True,
        "showTodayButton": True,
        "allowInputToggle": True,
        'locale': 'ru',

    },
    # You can set date and event hook options using JavaScript, usage in README.
    # You can also set options for specific variant widgets only which overrides above options.
    "variant_options": {
        "date": {
            "format": "MM/DD/YYYY",
        },
        "datetime": {
            "format": "MM/DD/YYYY HH:mm",
        },
        "month": {
            "format": "MMMM, YYYY",
        },
    },
    #
    # HTML attributes for widget <input> element
    # "attrs": {
    #     "class": "input",
    # },
    #
    # Override input addon icon classes
    "addon_icon_classes": {
        "month": "bi-calendar-month",
    },
    #
    # HTML template to render the html input
    # example: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/5.0.0/dev/myapp/templates/myapp/custom-input.html
    #
    # "template_name": "your-app/custom-input.html",
    #
    # Advanced: Choose where from static JS/CSS files are served.
    # defaults: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/5.0.0/src/bootstrap_datepicker_plus/settings.py#L16
    # To serve from any other preferred CDN, just update the options below.
    # You can also set them to None if you already have the following resources
    # included into your template.
    #
    # "datetimepicker_js_url": "https://..",
    # "datetimepicker_css_url": "https://..",
    # "momentjs_url": None,  # If you already have momentjs added into your template
    # "bootstrap_icon_css_url": None,  # If you don't need bootstrap icons
    #
    # If you want to serve static files yourself without CDN (from staticfiles) and
    # you know how to serve django static files on production server (DEBUG=False)
    # Then download the js/css files to any of your static directory, update the js/css
    # urls above and set the following option
    #
    # "app_static_url": "bootstrap_datepicker_plus/",
}
