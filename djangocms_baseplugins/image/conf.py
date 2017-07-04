# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset, \
    build_baseplugin_widgets

IMAGEPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_DESIGN_FIELDS', [])

IMAGEPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption',
    )
)

IMAGEPLUGIN_FIELDSETS = getattr(
    settings,
    'IMAGEPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': IMAGEPLUGIN_DESIGN_FIELDS,
        'content': IMAGEPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)


IMAGEPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'IMAGEPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"), ),
        ('content', _("Content Sized"), ),
    )
)


IMAGEPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'IMAGEPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"), ),
    )
)


IMAGEPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'IMAGEPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"), ),
    )
)

