from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.gallery.models import Gallery
from . import conf

translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS \
                     + conf.GALLERYPLUGIN_TRANSLATED_FIELDS


class GalleryTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('gallery')
    translator.register(Gallery, GalleryTranslationOptions)
