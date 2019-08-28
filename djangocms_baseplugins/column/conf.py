# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

COLUMNPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'COLUMNPLUGIN_TRANSLATED_FIELDS', [])

COLUMNPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'COLUMNPLUGIN_CONTENT_FIELDS', [])

COLUMNPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'COLUMNPLUGIN_DESIGN_FIELDS', [])

COLUMNPLUGIN_FIELDSETS = getattr(
    settings,
    'COLUMNPLUGIN_FIELDSETS ',
    build_baseplugin_fieldset(**{
        'content': COLUMNPLUGIN_CONTENT_FIELDS,
        'design': COLUMNPLUGIN_DESIGN_FIELDS,
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
