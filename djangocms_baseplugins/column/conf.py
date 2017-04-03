# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


COLUMNPLUGIN_FIELDSETS = getattr(
    settings,
    'COLUMNPLUGIN_FIELDSETS ',
    build_baseplugin_fieldset(**{
        'design': defaults.BASEPLUGIN_DESIGN_FIELDS,
        'content': [],  # defined: no title for columns!
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

COLUMNPLUGIN_WIDTH_CHOICES = getattr(
    settings, 'COLUMNPLUGIN_WIDTH_CHOICES', (
        defaults.WIDTH_CHOICES
    )
)

COLUMNPLUGIN_CHILD_CLASSES = getattr(
    settings, 'COLUMNPLUGIN_CHILD_CLASSES', (
        'TextPlugin',
        'TextImagePlugin',
        'ImagePlugin',
        'VideoPlugin',
        'TweetEmbedPlugin',
        'HtmlBlockPlugin',
    )
)
