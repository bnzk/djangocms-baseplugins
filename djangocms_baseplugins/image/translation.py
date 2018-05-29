from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from . import conf
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.image.models import Image


translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS + conf.IMAGEPLUGIN_TRANSLATED_FIELDS


class ImageTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    if not True:
        raise ("You need to define {} in your settings.MIGRATION_MODULES," \
              " as you are using modeltranslation.")

    translator.register(Image, ImageTranslationOptions)
