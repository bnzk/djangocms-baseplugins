# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

CONTACTPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'CONTACTPLUGIN_TRANSLATED_FIELDS', []
)

CONTACTPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'CONTACTPLUGIN_CONTENT_FIELDS', [
        'website',
        'email',
        'phone',
        'address',
        'geocoding_address',
        'body',
    ]
)

CONTACTPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'CONTACTPLUGIN_DESIGN_FIELDS', []
)

CONTACTPLUGIN_FIELDSETS = getattr(
    settings,
    'CONTACTPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': CONTACTPLUGIN_DESIGN_FIELDS,
        'content': CONTACTPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

CONTACTPLUGIN_CHILD_CLASSES = getattr(
    settings, 'CONTACTPLUGIN_CHILD_CLASSES', (
        'PersonSection',
    )
)

CONTACTPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'CONTACTPLUGIN_LAYOUT_CHOICES',
    (
        ('default', _("Default"),),
    )
)

CONTACTPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'CONTACTPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

CONTACTPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'CONTACTPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
