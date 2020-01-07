# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

SLIDERPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'SLIDERPLUGIN_TRANSLATED_FIELDS', []
)

SLIDERPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'SLIDERPLUGIN_CONTENT_FIELDS', []
)

SLIDERPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'SLIDERPLUGIN_DESIGN_FIELDS', []
)

SLIDERPLUGIN_FIELDSETS = getattr(
    settings,
    'SLIDERPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': SLIDERPLUGIN_DESIGN_FIELDS,
        'content': SLIDERPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

SLIDERPLUGIN_CHILD_CLASSES = getattr(
    settings, 'SLIDERPLUGIN_CHILD_CLASSES', (
        'ImagePlugin',
        'TextImagePlugin',
    )
)

SLIDERPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'SLIDERPLUGIN_LAYOUT_CHOICES',
    (
        ('default', _("Default"),),
    )
)

SLIDERPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'SLIDERPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

SLIDERPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'SLIDERPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
