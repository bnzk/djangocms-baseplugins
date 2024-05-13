from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults

from . import conf
from .models import Contact

translation_fields = defaults.TRANSLATED_FIELDS + conf.TRANSLATED_FIELDS


class ContactTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, "DJANGOCMS_BASEPLUGINS_TRANSLATE", None):
    translator.register(Contact, ContactTranslationOptions)
