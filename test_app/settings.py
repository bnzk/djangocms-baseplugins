"""Settings that need to be set in order to run the tests."""
import os
import tempfile
import logging


DJANGOCMS_BASEPLUGINS_MODE = 'minimal'

CMS_TEMPLATES = (
    ('base.html', 'Default'),
)


##################333333

DEBUG = True

logging.getLogger("factory").setLevel(logging.WARN)

SITE_ID = 1
TIME_ZONE = 'Europe/Zurich'

APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
    }
}

LANGUAGES = (
    ('en', 'EN', ),
    ('de', 'DE', ),
    ('fr', 'FR', ),
)
LANGUAGE_CODE = 'de'

ROOT_URLCONF = 'test_app.urls'

# media root is overridden when needed in tests
MEDIA_ROOT = os.path.join(APP_ROOT, '../test_app_media')
MEDIA_URL = "/media/"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../test_app_static')
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

#TEMPLATE_DIRS = (
#    os.path.join(APP_ROOT, 'tests/test_app/templates'),
#)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
            ],
        }
    },
]

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.join(APP_ROOT, 'tests/coverage'))
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = (
    # 'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    'ckeditor',
    'mailprotector',

    'filer',
    'easy_thumbnails',

    'cms',
    'menus',
    'classytags',
    'treebeard',
    'sekizai',
    'djangocms_admin_style',

    'django.contrib.admin',

)

INTERNAL_APPS = (
    'test_app',
    'djangocms_baseplugins',
    'djangocms_baseplugins.baseplugin',
    'djangocms_baseplugins.text',
    'djangocms_baseplugins.image',
    'djangocms_baseplugins.gallery',
    'djangocms_baseplugins.gallery_inline',
    'djangocms_baseplugins.section',
    'djangocms_baseplugins.column',
    'djangocms_baseplugins.htmlblock',
    'djangocms_baseplugins.person',
    'djangocms_baseplugins.slider',
    'djangocms_baseplugins.teaser_section',
    'djangocms_baseplugins.textimage',
    'djangocms_baseplugins.twitter',
    'djangocms_baseplugins.video',
    'djangocms_baseplugins.spacer',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    # django cms specific
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

MIDDLEWARE = MIDDLEWARE_CLASSES

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

SECRET_KEY = 'foobarXXXxxsvXY'
