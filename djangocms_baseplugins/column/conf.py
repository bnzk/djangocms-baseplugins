# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


TRANSLATED_FIELDS = getattr(
    settings, 'COLUMNPLUGIN_TRANSLATED_FIELDS', [])

CONTENT_FIELDS = getattr(
    settings, 'COLUMNPLUGIN_CONTENT_FIELDS', [])

DESIGN_FIELDS = getattr(
    settings, 'COLUMNPLUGIN_DESIGN_FIELDS', [])

FIELDSETS = getattr(
    settings,
    'COLUMNPLUGIN_FIELDSETS ',
    get_baseplugin_fieldset(**{
        'content': CONTENT_FIELDS,
        'design': DESIGN_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

WIDTH_CHOICES = getattr(
    settings, 'COLUMNPLUGIN_WIDTH_CHOICES', (
        defaults.WIDTH_CHOICES
    )
)

CHILD_CLASSES = getattr(
    settings, 'COLUMNPLUGIN_CHILD_CLASSES', (
        'TextPlugin',
        'TextImagePlugin',
        'ImagePlugin',
        'VideoPlugin',
        'TweetEmbedPlugin',
        'HtmlBlockPlugin',
    )
)

LAYOUT_CHOICES = getattr(
    settings,
    'COLUMNPLUGIN_LAYOUT_CHOICES',
    (
        ('2whatwhat', _("2 Spalten"),),
        ('3', _("3 Spalten"),),
        ('4', _("4 Spalten"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'COLUMNPLUGIN_BACKGROUND_CHOICES',
    (
        ('white', _("Weiss"),),
        ('beige', _("Beige"),),
        ('grey', _("Grau"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'COLUMNPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
