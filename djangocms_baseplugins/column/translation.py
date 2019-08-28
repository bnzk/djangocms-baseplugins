from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.column.models import Column
from . import conf

translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS \
                     + conf.COLUMNPLUGIN_TRANSLATED_FIELDS


class ColumnPluginTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('column')
    translator.register(Column, ColumnPluginTranslationOptions)
