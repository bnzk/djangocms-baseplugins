from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from . import conf
from .models import HtmlBlock

translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.HTMLBLOCKPLUGIN_TRANSLATED_FIELDS


class HtmlBlockTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('htmlblock')
    translator.register(HtmlBlock, HtmlBlockTranslationOptions)
