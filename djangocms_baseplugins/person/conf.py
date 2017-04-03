# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


PERSONSECTIONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'PERSONSECTIONPLUGIN_CONTENT_FIELDS', (
        defaults.BASEPLUGIN_CONTENT_FIELDS,
    )
)

PERSONSECTIONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'PERSONSECTIONPLUGIN_DESIGN_FIELDS', []
)

PERSONSECTIONPLUGIN_FIELDSETS = getattr(
    settings,
    'PERSONSECTIONPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': PERSONSECTIONPLUGIN_DESIGN_FIELDS,
        'content': PERSONSECTIONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)


PERSONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'PERSONPLUGIN_CONTENT_FIELDS', (
        'image', 'title', ('salutation', 'first_name', 'last_name', ), 'body', 'email', 'phone', 'website',
    )
)

PERSONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'PERSONPLUGIN_DESIGN_FIELDS', []
)

PERSONPLUGIN_FIELDSETS = getattr(
    settings,
    'PERSONPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': PERSONPLUGIN_DESIGN_FIELDS,
        'content': PERSONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

