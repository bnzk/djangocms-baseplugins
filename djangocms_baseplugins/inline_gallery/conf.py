# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

INLINEGALLERYPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'INLINEGALLERYPLUGIN_TRANSLATED_FIELDS', [])

INLINEGALLERYPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'INLINEGALLERYPLUGIN_CONTENT_FIELDS', [])

INLINEGALLERYPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'INLINEGALLERYPLUGIN_DESIGN_FIELDS', [])

INLINEGALLERYPLUGIN_FIELDSETS = getattr(
    settings,
    'INLINEGALLERYPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'content': INLINEGALLERYPLUGIN_CONTENT_FIELDS,
        'design': INLINEGALLERYPLUGIN_DESIGN_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

INLINEGALLERYPLUGIN_CHILD_CLASSES = getattr(
    settings, 'INLINEGALLERYPLUGIN_CHILD_CLASSES', (
        'ImagePlugin',
        'TextImagePlugin',
    )
)
