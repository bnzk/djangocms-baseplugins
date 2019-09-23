# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

SPACERPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'SPACERPLUGIN_TRANSLATED_FIELDS', [])

SPACERPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'SPACERPLUGIN_CONTENT_FIELDS', [])

SPACERPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'SPACERPLUGIN_DESIGN_FIELDS', ['layout'])

SPACERPLUGIN_FIELDSETS = getattr(
    settings,
    'SPACERPLUGIN_FIELDSETS ',
    build_baseplugin_fieldset(**{
        'content': SPACERPLUGIN_CONTENT_FIELDS,
        'design': SPACERPLUGIN_DESIGN_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

SPACERPLUGIN_LAYOUT_CHOICES = getattr(
    settings, 'SPACERPLUGIN_LAYOUT_CHOICES', (
        ('remove-one', _("Remove space")),
        ('remove-half', _("Remove half space")),
        ('', ("-")),
        ('add-half', _("Add little more space")),
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
