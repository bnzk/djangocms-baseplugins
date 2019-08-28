from .settings import *  # noqa


INSTALLED_APPS = ('modeltranslation', 'djangocms_misc.basic') + INSTALLED_APPS  # noqa

DJANGOCMS_BASEPLUGINS_TRANSLATE = True

IMAGEPLUGIN_TRANSLATE_IMAGE = False

MIGRATION_MODULES = {
    'column': 'test_app.migrations.column',
    'gallery': 'test_app.migrations.gallery',
    'htmlblock': 'test_app.migrations.htmlblock',
    'image': 'test_app.migrations.image',
    'person': 'test_app.migrations.person',
    'section': 'test_app.migrations.section',
    'slider': 'test_app.migrations.slider',
    'spacer': 'test_app.migrations.spacer',
    'teaser_section': 'test_app.migrations.teaser_section',
    'text': 'test_app.migrations.text',
    'textimage': 'test_app.migrations.textimage',
    'twitter': 'test_app.migrations.twitter',
    'video': 'test_app.migrations.video',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite_modeltranslation.db',
    }
}
