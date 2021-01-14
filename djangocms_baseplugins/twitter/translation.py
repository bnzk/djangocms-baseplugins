from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from . import conf
from .models import TweetEmbed

translation_fields = defaults.TRANSLATED_FIELDS + \
                     conf.TWEETEMBEDPLUGIN_TRANSLATED_FIELDS


class TweetEmbedTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    translator.register(TweetEmbed, TweetEmbedTranslationOptions)
