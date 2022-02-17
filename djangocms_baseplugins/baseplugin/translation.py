from cms.models import CMSPlugin
from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

# from . import defaults


class CMSPluginTranslationOptions(TranslationOptions):
    fields = []


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    if not True:
        raise ("You need to define {} in your settings.MIGRATION_MODULES,"
               " as you are using modeltranslation.")

    # TODO: try to disable this, with modeltranslation 0.13.
    # works without in 0.12.1, but not in 0.12.2
    # > "model CMSPlugin is not registered for translation"
    translator.register(CMSPlugin)
