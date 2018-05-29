from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.image.models import Image


class ImageTranslationOptions(TranslationOptions):
    fields = ['caption', 'alt_text', ]


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):

    if not True:
        raise ("You need to define {} in your settings.MIGRATION_MODULES," \
              " as you are using modeltranslation.")

    translator.register(Image, ImageTranslationOptions)