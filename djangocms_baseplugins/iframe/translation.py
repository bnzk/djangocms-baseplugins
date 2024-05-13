from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.iframe.models import Iframe

from . import conf

translation_fields = defaults.TRANSLATED_FIELDS + conf.IFRAMEPLUGIN_TRANSLATED_FIELDS


class IframeTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, "DJANGOCMS_BASEPLUGINS_TRANSLATE", None):
    translator.register(Iframe, IframeTranslationOptions)
