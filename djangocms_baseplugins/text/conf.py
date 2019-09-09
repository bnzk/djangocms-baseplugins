# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


print('loaded!----------------------------------------------')

# clean when saving? default is to clean on render AND save.
TEXTPLUGIN_CLEAN_ON_SAVE = getattr(
    settings,
    'TEXTPLUGIN_CLEAN_ON_SAVE',
    True,
)

TEXTPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'TEXTPLUGIN_TRANSLATED_FIELDS', [
        'body',
    ]
)

TEXTPLUGIN_LAYOUT_CHOICES = getattr(
    settings, 'TEXTPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

TEXTPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'TEXTPLUGIN_CONTENT_FIELDS', (
        'body',
    )
)

TEXTPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'TEXTPLUGIN_DESIGN_FIELDS', []
)

TEXTPLUGIN_FIELDSETS = getattr(
    settings,
    'TEXTPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': TEXTPLUGIN_DESIGN_FIELDS,
        'content': TEXTPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)
