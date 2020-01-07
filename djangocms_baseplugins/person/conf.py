# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

PERSONSECTIONPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'PERSONSECTIONPLUGIN_TRANSLATED_FIELDS', []
)

PERSONSECTIONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'PERSONSECTIONPLUGIN_CONTENT_FIELDS', []
)

PERSONSECTIONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'PERSONSECTIONPLUGIN_DESIGN_FIELDS', []
)

PERSONSECTIONPLUGIN_FIELDSETS = getattr(
    settings,
    'PERSONSECTIONPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': PERSONSECTIONPLUGIN_DESIGN_FIELDS,
        'content': PERSONSECTIONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

PERSONSECTIONPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'PERSONSECTIONPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

PERSONSECTIONPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'PERSONSECTIONPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

PERSONSECTIONPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'PERSONSECTIONPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)

PERSONPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'PERSONPLUGIN_TRANSLATED_FIELDS',
    ['salutation', 'function', 'department', 'body', ]
)

PERSONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'PERSONPLUGIN_CONTENT_FIELDS', (
        'image',
        ('title', 'function', 'department',),
        ('salutation', 'first_name', 'last_name',),
        'body',
        'email',
        'phone',
        'website',
    )
)

PERSONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'PERSONPLUGIN_DESIGN_FIELDS', []
)

PERSONPLUGIN_FIELDSETS = getattr(
    settings,
    'PERSONPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': PERSONPLUGIN_DESIGN_FIELDS,
        'content': PERSONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

PERSONPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'PERSONPLUGIN__LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)

PERSONPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'PERSONPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

PERSONPLUGIN__COLOR_CHOICES = getattr(
    settings,
    'PERSONPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
