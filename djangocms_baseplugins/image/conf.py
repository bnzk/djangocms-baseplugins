# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_TRANSLATED_FIELDS',
    ['caption', 'alt_text', ]
)

DESIGN_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_DESIGN_FIELDS', [])

CONTENT_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption',
    )
)

FIELDSETS = getattr(
    settings,
    'IMAGEPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

LAYOUT_CHOICES = getattr(
    settings,
    'IMAGEPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'IMAGEPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'IMAGEPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
