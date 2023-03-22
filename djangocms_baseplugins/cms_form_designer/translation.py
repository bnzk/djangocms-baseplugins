from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from .models import FormDesigner
from . import conf


translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf.TRANSLATED_FIELDS


class FormDesignerTranslationOptions(TranslationOptions):
    fields = translation_fields


translator.register(FormDesigner, FormDesignerTranslationOptions)
