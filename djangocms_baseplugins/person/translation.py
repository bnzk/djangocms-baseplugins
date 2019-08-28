from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.person.models import Person, PersonSection
from . import conf

translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS \
                     + conf.PERSONPLUGIN_TRANSLATED_FIELDS


class PersonTranslationOptions(TranslationOptions):
    fields = translation_fields


translation_fields = defaults.DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS \
                     + conf.PERSONSECTIONPLUGIN_TRANSLATED_FIELDS


class PersonSectionTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('person')
    translator.register(Person, PersonTranslationOptions)
    translator.register(PersonSection, PersonSectionTranslationOptions)
