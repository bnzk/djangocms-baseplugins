from cms.models import CMSPlugin
from djangocms_baseplugins.baseplugin import defaults
from . import defaults
from modeltranslation.translator import TranslationOptions, translator



class CMSPluginTranslationOptions(TranslationOptions):
    fields = []


if getattr(defaults, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    if not True:
        raise ("You need to define {} in your settings.MIGRATION_MODULES," \
              " as you are using modeltranslation.")

    # TODO: try to disable this, with modeltranslation 0.13. works without in 0.12.1, but not in 0.12.2
    # "model CMSPlugin is not registered for translation"
    translator.register(CMSPlugin)
