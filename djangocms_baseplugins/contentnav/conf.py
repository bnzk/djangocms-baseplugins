# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


TRANSLATED_FIELDS = getattr(
    settings, 'CONTENTNAVPLUGIN_TRANSLATED_FIELDS', [])

CONTENT_FIELDS = getattr(
    settings,
    'CONTENTNAVPLUGIN_CONTENT_FIELDS',
    ['menu_depth', 'cms_page', 'sitemap', ],
)

DESIGN_FIELDS = getattr(
    settings, 'CONTENTNAVPLUGIN_DESIGN_FIELDS', [])

FIELDSETS = getattr(
    settings,
    'CONTENTNAVPLUGIN_FIELDSETS ',
    get_baseplugin_fieldset(**{
        'content': CONTENT_FIELDS,
        'design': DESIGN_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

LAYOUT_CHOICES = getattr(
    settings,
    'CONTENTNAVPLUGIN_LAYOUT_CHOICES',
    (
        ('default', _("Default"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'CONTENTNAVPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'CONTENTNAVPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
