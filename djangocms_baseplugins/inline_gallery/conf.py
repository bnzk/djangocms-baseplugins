# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

INLINEGALLERYPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'INLINEGALLERYPLUGIN_TRANSLATED_FIELDS', ['description', ])

INLINEGALLERYPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'INLINEGALLERYPLUGIN_CONTENT_FIELDS', [])

INLINEGALLERYPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'INLINEGALLERYPLUGIN_DESIGN_FIELDS', [])

INLINEGALLERYPLUGIN_FIELDSETS = getattr(
    settings,
    'INLINEGALLERYPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'content': INLINEGALLERYPLUGIN_CONTENT_FIELDS,
        'design': INLINEGALLERYPLUGIN_DESIGN_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

INLINEGALLERYPLUGIN_IMAGE_CONTENT_FIELDS = getattr(
    settings,
    'INLINEGALLERYPLUGIN_IMAGE_CONTENT_FIELDS',
    ['image', ('order', 'caption',)]
)


INLINEGALLERYPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'INLINEGALLERYPLUGIN_LAYOUT_CHOICES',
    (
        ('default', ("Default"),),
    )
)

INLINEGALLERYPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'INLINEGALLERYPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', ("Default"),),
    )
)

INLINEGALLERYPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'INLINEGALLERYPLUGIN_COLOR_CHOICES',
    (
        ('default', ("Default"),),
    )
)
