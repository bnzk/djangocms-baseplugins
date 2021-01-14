from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.image.models import Image
from . import conf

translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.TRANSLATED_FIELDS


class ImageTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    translator.register(Image, ImageTranslationOptions)
