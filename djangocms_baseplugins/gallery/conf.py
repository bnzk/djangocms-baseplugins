# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


GALLERYPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'GALLERYPLUGIN_TRANSLATED_FIELDS', ['description', ])

GALLERYPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'GALLERYPLUGIN_CONTENT_FIELDS', [])

GALLERYPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'GALLERYPLUGIN_DESIGN_FIELDS', [])

GALLERYPLUGIN_FIELDSETS = getattr(
    settings,
    'GALLERYPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'content': GALLERYPLUGIN_CONTENT_FIELDS,
        'design': GALLERYPLUGIN_DESIGN_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

GALLERYPLUGIN_CHILD_CLASSES = getattr(
    settings, 'GALLERYPLUGIN_CHILD_CLASSES', (
        'ImagePlugin',
        'TextImagePlugin',
    )
)

GALLERYPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'GALLERYPLUGIN_LAYOUT_CHOICES',
    (
        ('default', "Default",),
    )
)

GALLERYPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'GALLERYPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', ("Default"),),
    )
)

GALLERYPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'GALLERYPLUGIN_COLOR_CHOICES',
    (
        ('default', ("Default"),),
    )
)
