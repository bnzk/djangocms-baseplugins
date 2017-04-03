# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


SECTIONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'SECTIONPLUGIN_CONTENT_FIELDS', []
)

SECTIONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'SECTIONPLUGIN_DESIGN_FIELDS', []
)

SECTIONPLUGIN_FIELDSETS = getattr(
    settings,
    'SECTIONPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': SECTIONPLUGIN_DESIGN_FIELDS,
        'content': SECTIONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

SECTIONPLUGIN_CHILD_CLASSES = getattr(
    settings, 'SECTIONPLUGIN_CHILD_CLASSES', (
        'ColumnPlugin',
    )
)
