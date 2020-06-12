# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


CLEAN_ON_SAVE = getattr(
    settings,
    'TEXTIMAGEPLUGIN_CLEAN_ON_SAVE',
    True,
)

TRANSLATED_FIELDS = getattr(
    settings, 'TEXTIMAGEPLUGIN_TRANSLATED_FIELDS', [
        'caption', 'body',
    ]
)

LAYOUT_CHOICES = getattr(
    settings, 'TEXTIMAGEPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

BACKGROUND_CHOICES = getattr(
    settings, 'TEXTIMAGEPLUGIN_BACKGROUND_CHOICES', (
        [],
    )
)

COLOR_CHOICES = getattr(
    settings, 'TEXTIMAGEPLUGIN_COLOR_CHOICES', (
        [],
    )
)

CONTENT_FIELDS = getattr(
    settings, 'TEXTIMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption', 'body',
    )
)

DESIGN_FIELDS = getattr(
    settings, 'TEXTIMAGEPLUGIN_DESIGN_FIELDS', []
)

FIELDSETS = getattr(
    settings,
    'TEXTIMAGEPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

IMAGE_REQUIRED = getattr(
    settings, 'TEXTIMAGEPLUGIN_IMAGE_REQUIRED', True
)

REQUIRE_PARENT = getattr(
    settings,
    'TEXTIMAGEPLUGIN_REQUIRE_PARENT',
    False,
)
