# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'HTMLBLOCKPLUGIN_TRANSLATED_FIELDS', ['htmlblock', ])

DESIGN_FIELDS = getattr(
    settings, 'HTMLBLOCKPLUGIN_DESIGN_FIELDS', [])

CONTENT_FIELDS = getattr(
    settings, 'HTMLBLOCKPLUGIN_CONTENT_FIELDS', (
        'htmlblock',
    )
)

FIELDSETS = getattr(
    settings,
    'HTMLBLOCKPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })

)

LAYOUT_CHOICES = getattr(
    settings,
    'HTMLBLOCKPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'HTMLBLOCKPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'HTMLBLOCKPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
