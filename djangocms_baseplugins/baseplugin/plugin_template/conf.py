# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_TRANSLATED_FIELDS',
    ['caption', ]
)

DESIGN_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_DESIGN_FIELDS', [
        'layout',
    ])

CONTENT_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_CONTENT_FIELDS', (
        'image',
        'caption',
    )
)

FIELDSETS = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

LAYOUT_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
