from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from . import conf
from .models import Spacer

translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS + \
                     conf.SPACERPLUGIN_TRANSLATED_FIELDS


class SpacerTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('slider')
    translator.register(Spacer, SpacerTranslationOptions)
