from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.download.models import Download, DownloadSection

from . import conf_entry, conf_section

# section
section_translation_fields = defaults.TRANSLATED_FIELDS + conf_section.TRANSLATED_FIELDS


class DownloadSectionTranslationOptions(TranslationOptions):
    fields = section_translation_fields


if getattr(settings, "DJANGOCMS_BASEPLUGINS_TRANSLATE", None):
    translator.register(DownloadSection, DownloadSectionTranslationOptions)


# entry
translation_fields = defaults.TRANSLATED_FIELDS + conf_entry.TRANSLATED_FIELDS


class DownloadTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, "DJANGOCMS_BASEPLUGINS_TRANSLATE", None):
    translator.register(Download, DownloadTranslationOptions)
