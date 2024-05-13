from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults

from . import conf
from .models import TextImage


class TextImageTranslationOptions(TranslationOptions):
    fields = defaults.TRANSLATED_FIELDS + conf.TRANSLATED_FIELDS


if getattr(settings, "DJANGOCMS_BASEPLUGINS_TRANSLATE", None):
    translator.register(TextImage, TextImageTranslationOptions)
