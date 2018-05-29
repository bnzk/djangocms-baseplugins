from .settings import *  # noqa


INSTALLED_APPS = INSTALLED_APPS + ('modeltranslation', )

DJANGOCMS_BASEPLUGINS_TRANSLATE = True

IMAGEPLUGIN_TRANSLATE_IMAGE = False

MIGRATION_MODULES = {
    'column': 'djangocms_baseplugins.tests.test_app.migrations.column',
    'gallery': 'djangocms_baseplugins.tests.test_app.migrations.gallery',
    'htmlblock': 'djangocms_baseplugins.tests.test_app.migrations.htmlblock',
    'image': 'djangocms_baseplugins.tests.test_app.migrations.image',
    'person': 'djangocms_baseplugins.tests.test_app.migrations.person',
    'section': 'djangocms_baseplugins.tests.test_app.migrations.section',
    'slider': 'djangocms_baseplugins.tests.test_app.migrations.slider',
    'spacer': 'djangocms_baseplugins.tests.test_app.migrations.spacer',
    'teaser_section': 'djangocms_baseplugins.tests.test_app.migrations.teaser_section',
    'text': 'djangocms_baseplugins.tests.test_app.migrations.text',
    'textimage': 'djangocms_baseplugins.tests.test_app.migrations.textimage',
    'twitter': 'djangocms_baseplugins.tests.test_app.migrations.twitter',
    'video': 'djangocms_baseplugins.tests.test_app.migrations.video',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite_modeltranslation.db',
    }
}
