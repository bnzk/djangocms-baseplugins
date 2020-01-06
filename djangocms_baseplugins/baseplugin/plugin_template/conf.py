# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

PLUGINTEMPLATEPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_TRANSLATED_FIELDS',
    ['caption', 'alt_text', ]
)

PLUGINTEMPLATEPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_DESIGN_FIELDS', [])

PLUGINTEMPLATEPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_CONTENT_FIELDS', (
        'plugintemplate', 'caption',
    )
)

PLUGINTEMPLATEPLUGIN_FIELDSETS = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': PLUGINTEMPLATEPLUGIN_DESIGN_FIELDS,
        'content': PLUGINTEMPLATEPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

PLUGINTEMPLATEPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

PLUGINTEMPLATEPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

PLUGINTEMPLATEPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
