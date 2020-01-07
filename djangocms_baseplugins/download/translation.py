from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.download.models import Download, DownloadSection
from . import conf

translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.DOWNLOADPLUGIN_TRANSLATED_FIELDS


class DownloadTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('download')
    translator.register(Download, DownloadTranslationOptions)

section_translation_fields = defaults.TRANSLATED_FIELDS \
                             + conf.DOWNLOADPLUGIN_TRANSLATED_FIELDS


class DownloadSectionTranslationOptions(TranslationOptions):
    fields = section_translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('download')
    translator.register(DownloadSection, DownloadSectionTranslationOptions)
