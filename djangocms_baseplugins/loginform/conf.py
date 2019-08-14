# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset



LOGINFORMPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'LOGINFORMPLUGIN_TRANSLATED_FIELDS',
    []
)

LOGINFORMPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'LOGINFORMPLUGIN_DESIGN_FIELDS', []
)

LOGINFORMPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'LOGINFORMPLUGIN_CONTENT_FIELDS', []
)

LOGINFORMPLUGIN_FIELDSETS = getattr(
    settings,
    'LOGINFORMPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': LOGINFORMPLUGIN_DESIGN_FIELDS,
        'content': LOGINFORMPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)
