from django.conf import settings
from modeltranslation.translator import TranslationOptions, translator

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_in_migration_modules
from djangocms_baseplugins.person.models import Person, PersonSection
from . import conf_section, conf_person


translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf_person.TRANSLATED_FIELDS


class PersonTranslationOptions(TranslationOptions):
    fields = translation_fields


translation_fields = defaults.TRANSLATED_FIELDS \
                     + conf_section.TRANSLATED_FIELDS


class PersonSectionTranslationOptions(TranslationOptions):
    fields = translation_fields


if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
    check_in_migration_modules('person')
    translator.register(Person, PersonTranslationOptions)
    translator.register(PersonSection, PersonSectionTranslationOptions)
