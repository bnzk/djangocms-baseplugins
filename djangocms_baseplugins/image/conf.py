# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


IMAGEPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_DESIGN_FIELDS', [])

IMAGEPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption',
    )
)

IMAGEPLUGIN_FIELDSETS = getattr(
    settings,
    'IMAGEPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': IMAGEPLUGIN_DESIGN_FIELDS,
        'content': IMAGEPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)
