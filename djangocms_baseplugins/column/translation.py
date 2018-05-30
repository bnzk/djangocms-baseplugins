from django.conf import settings

from modeltranslation.translator import TranslationOptions, translator

from . import conf
from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.column.models import Column


translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS + conf.COLUMNPLUGIN_TRANSLATED_FIELDS


class ColumnPluginTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    if not True:
        raise ("You need to define {} in your settings.MIGRATION_MODULES," \
              " as you are using modeltranslation.")

    translator.register(Column, ColumnPluginTranslationOptions)
