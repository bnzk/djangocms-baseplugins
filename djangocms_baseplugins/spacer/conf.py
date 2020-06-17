# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'SPACERPLUGIN_TRANSLATED_FIELDS', [])

CONTENT_FIELDS = getattr(
    settings, 'SPACERPLUGIN_CONTENT_FIELDS', [])

DESIGN_FIELDS = getattr(
    settings, 'SPACERPLUGIN_DESIGN_FIELDS', ['layout'])

FIELDSETS = getattr(
    settings,
    'SPACERPLUGIN_FIELDSETS ',
    get_baseplugin_fieldset(**{
        'content': CONTENT_FIELDS,
        'design': DESIGN_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

LAYOUT_CHOICES = getattr(
    settings, 'SPACERPLUGIN_LAYOUT_CHOICES', (
        ('remove-one', _("Remove space")),
        ('remove-half', _("Remove half space")),
        ('', ("-")),
        ('add-half', _("Add half space")),
        ('add-one', _("Add space")),
        ('add-double', _("Add double space")),
        ('add-triple', _("Add triple space")),
        # orig
        # ('remove-all-space', _("Remove space")),
        # ('remove-half-space', _("Remove half space")),
        # ('add-some-more-space', _("Add little more space")),
        # ('add-normal-space', _("Add normal space")),
        # ('add-double-normal-space', _("Add double of normal space")),
        # ('add-triple-normal-space', _("Add triple of normal space")),
    )
)

BACKGROUND_CHOICES = getattr(
    settings, 'SPACERPLUGIN_BACKGROUND_CHOICES', (
        ('', ("-")),
    )
)

COLOR_CHOICES = getattr(
    settings, 'SPACERPLUGIN_COLOR_CHOICES', (
        ('', ("-")),
    )
)
