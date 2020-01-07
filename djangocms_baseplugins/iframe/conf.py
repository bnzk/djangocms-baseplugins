# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'IFRAMEPLUGIN_TRANSLATED_FIELDS',
    []
)

DESIGN_FIELDS = getattr(
    settings, 'IFRAMEPLUGIN_DESIGN_FIELDS', [
        'layout',
    ])

CONTENT_FIELDS = getattr(
    settings, 'IFRAMEPLUGIN_CONTENT_FIELDS', (
        'iframe_url',
    )
)

FIELDSETS = getattr(
    settings,
    'IFRAMEPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

LAYOUT_CHOICES = getattr(
    settings,
    'IFRAMEPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'IFRAMEPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'IFRAMEPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
