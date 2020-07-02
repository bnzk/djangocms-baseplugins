from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from . import conf
from .models import Video


translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.TRANSLATED_FIELDS


class VideoTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('video')
    translator.register(Video, VideoTranslationOptions)
