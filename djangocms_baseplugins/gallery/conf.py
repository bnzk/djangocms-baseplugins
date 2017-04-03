# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

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
