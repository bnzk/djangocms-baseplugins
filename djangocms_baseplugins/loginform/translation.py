from djangocms_baseplugins.baseplugin import defaults
from modeltranslation.translator import TranslationOptions, translator

from .models import LoginForm



translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS


class LoginFormTranslationOptions(TranslationOptions):
    fields = translation_fields


translator.register(LoginForm, LoginFormTranslationOptions)

