from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from .models import LoginForm


translation_fields = defaults.TRANSLATED_FIELDS


class LoginFormTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    translator.register(LoginForm, LoginFormTranslationOptions)
