from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from .models import AutoColumns
from . import conf


class AutoColumnsPluginTranslationOptions(TranslationOptions):
    fields = defaults.TRANSLATED_FIELDS + conf.TRANSLATED_FIELDS


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('autocolumns')
    translator.register(AutoColumns, AutoColumnsPluginTranslationOptions)
