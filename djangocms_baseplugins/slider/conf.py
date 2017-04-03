# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

SLIDERPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'SLIDERPLUGIN_CONTENT_FIELDS', []
)

SLIDERPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'SLIDERPLUGIN_DESIGN_FIELDS', []
)

SLIDERPLUGIN_FIELDSETS = getattr(
    settings,
    'SLIDERPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': SLIDERPLUGIN_DESIGN_FIELDS,
        'content': SLIDERPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

SLIDERPLUGIN_CHILD_CLASSES = getattr(
    settings, 'SLIDERPLUGIN_CHILD_CLASSES', (
        'ImagePlugin',
        'TextImagePlugin',
    )
)
