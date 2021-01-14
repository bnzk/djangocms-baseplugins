from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.column.models import Column
from . import conf

translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.TRANSLATED_FIELDS


class ColumnPluginTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(defaults, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    translator.register(Column, ColumnPluginTranslationOptions)
