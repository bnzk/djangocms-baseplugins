# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


# basics
NAME = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_NAME', _('Auto Columns')
)
MODULE = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_MODULE', defaults.CONTAINER_LABEL,
)


# parent / children
ALLOW_CHILDREN = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_ALLOW_CHILDREN', True
)
CHILD_CLASSES = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_CHILD_CLASSES', [
        'TextPlugin',
        'TextImagePlugin',
    ]
)
REQUIRE_PARENT = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_REQUIRE_PARENT', False
)


# fields
TRANSLATED_FIELDS = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_TRANSLATED_FIELDS', []
)
CONTENT_FIELDS = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_CONTENT_FIELDS', []
)
DESIGN_FIELDS = getattr(
    settings, 'AUTOCOLUMNSPLUGIN_DESIGN_FIELDS', ['layout', ]
)
FIELDSETS = getattr(
    settings,
    'AUTOCOLUMNSPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)


# choices
LAYOUT_CHOICES = getattr(
    settings,
    'AUTOCOLUMNSPLUGIN_LAYOUT_CHOICES',
    (
        ('2', _("2 Spalten"),),
        ('3', _("3 Spalten"),),
        ('4', _("4 Spalten"),),
    )
)
BACKGROUND_CHOICES = getattr(
    settings,
    'AUTOCOLUMNSPLUGIN_BACKGROUND_CHOICES',
    (
        ('white', _("Weiss"),),
        ('beige', _("Beige"),),
        ('grey', _("Grau"),),
    )
)
COLOR_CHOICES = getattr(
    settings,
    'AUTOCOLUMNSPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
