# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset



DOWNLOADSECTIONPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'DOWNLOADSECTIONPLUGIN_TRANSLATED_FIELDS',
    []
)

DOWNLOADSECTIONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'DOWNLOADSECTIONPLUGIN_DESIGN_FIELDS', []
)

DOWNLOADSECTIONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'DOWNLOADSECTIONPLUGIN_CONTENT_FIELDS', []
)

DOWNLOADSECTIONPLUGIN_FIELDSETS = getattr(
    settings,
    'DOWNLOADSECTIONPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': DOWNLOADSECTIONPLUGIN_DESIGN_FIELDS,
        'content': DOWNLOADSECTIONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

DOWNLOADSECTIONPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'DOWNLOADSECTIONPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"), ),
        ('content', _("Content Sized"), ),
    )
)

DOWNLOADSECTIONPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'DOWNLOADSECTIONPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"), ),
    )
)

DOWNLOADSECTIONPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'DOWNLOADSECTIONPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"), ),
    )
)

DOWNLOADSECTIONPLUGIN_CHILD_CLASSES = getattr(
    settings, 'DOWNLOADSECTIONPLUGIN_CHILD_CLASSES', (
        'DownloadPlugin',
    )
)



DOWNLOADPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'DOWNLOADPLUGIN_TRANSLATED_FIELDS',
    []
)

DOWNLOADPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'DOWNLOADPLUGIN_DESIGN_FIELDS', [])

DOWNLOADPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'DOWNLOADPLUGIN_CONTENT_FIELDS', (
        'file', 'link_text',
    )
)

DOWNLOADPLUGIN_FIELDSETS = getattr(
    settings,
    'DOWNLOADPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': DOWNLOADPLUGIN_DESIGN_FIELDS,
        'content': DOWNLOADPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

DOWNLOADPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'DOWNLOADPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"), ),
        ('content', _("Content Sized"), ),
    )
)

DOWNLOADPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'DOWNLOADPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"), ),
    )
)

DOWNLOADPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'DOWNLOADPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"), ),
    )
)


