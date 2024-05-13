from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults

from . import conf
from .models import Spacer

translation_fields = defaults.TRANSLATED_FIELDS + conf.TRANSLATED_FIELDS


class SpacerTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, "DJANGOCMS_BASEPLUGINS_TRANSLATE", None):
    translator.register(Spacer, SpacerTranslationOptions)
