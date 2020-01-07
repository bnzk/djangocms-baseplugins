from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.inline_gallery.models import InlineGallery
from . import conf

translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.INLINEGALLERYPLUGIN_TRANSLATED_FIELDS


class InlineGalleryTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('inline_gallery')
    translator.register(InlineGallery, InlineGalleryTranslationOptions)
