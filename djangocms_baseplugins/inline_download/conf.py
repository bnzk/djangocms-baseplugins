# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

INLINEDOWNLOADPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'INLINEDOWNLOADPLUGIN_TRANSLATED_FIELDS', [])

INLINEDOWNLOADPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'INLINEDOWNLOADPLUGIN_CONTENT_FIELDS', [])

INLINEDOWNLOADPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'INLINEDOWNLOADPLUGIN_DESIGN_FIELDS', [])

INLINEDOWNLOADPLUGIN_FIELDSETS = getattr(
    settings,
    'INLINEDOWNLOADPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'content': INLINEDOWNLOADPLUGIN_CONTENT_FIELDS,
        'design': INLINEDOWNLOADPLUGIN_DESIGN_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

INLINEDOWNLOADPLUGIN_ENTRY_CONTENT_FIELDS = getattr(
    settings, 'INLINEDOWNLOADPLUGIN_ENTRY_CONTENT_FIELDS', ['file', ('order', 'link_text',)])

# allow fallbacks!
INLINEDOWNLOADPLUGIN_ENTRY_TRANSLATED_FIELDS = getattr(
    settings, 'INLINEDOWNLOADPLUGIN_ENTRY_TRANSLATED_FIELDS', ['link_text', 'file'])

INLINEDOWNLOADPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'INLINEDOWNLOADPLUGIN_LAYOUT_CHOICES',
    (
        ('default', ("Default"),),
    )
)

INLINEDOWNLOADPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'INLINEDOWNLOADPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', ("Default"),),
    )
)

INLINEDOWNLOADPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'INLINEDOWNLOADPLUGIN_COLOR_CHOICES',
    (
        ('default', ("Default"),),
    )
)
