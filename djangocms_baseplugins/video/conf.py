# coding: utf-8
from __future__ import unicode_literals

import re

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'VIDEOPLUGIN_TRANSLATED_FIELDS', [
        'video_url',
    ]
)

# thx to rouxcode!
REGEXES = (
    re.compile(r'^https?\:\/\/(www\.)?youtu\.be\/(?P<youtube_id>[^\/]*)\??.*$'),
    re.compile(r'^https?\:\/\/(www\.)?youtube\.(com|nl|ru).*v=(?P<youtube_id>.*)\&?.*$'),
    re.compile(r'^https?\:\/\/(www\.)?youtube\.(com|nl|ru)\/embed\/(?P<youtube_id>[^\/]*)\??.*$'),
    re.compile(r'^https?\:\/\/(www\.)?vimeo\.com\/(?P<vimeo_id>[^\/]*)\??.*$'),
)

YOUTUBE_MODESTBRANDING = True

YOUTUBE_COLOR = 'red'  # or white
VIMEO_COLOR = False  # default blue

LAYOUT_CHOICES = getattr(
    settings, 'VIDEOPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

CONTENT_FIELDS = getattr(
    settings, 'VIDEOPLUGIN_CONTENT_FIELDS', (
        'video_url', ('show_related', 'autoplay', 'mute', 'controls', 'infos', 'fullscreen'),
    )
)

DESIGN_FIELDS = getattr(
    settings, 'VIDEOPLUGIN_DESIGN_FIELDS', []
)

FIELDSETS = getattr(
    settings,
    'VIDEOPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

LAYOUT_CHOICES = getattr(
    settings, 'VIDEOPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

BACKGROUND_CHOICES = getattr(
    settings, 'VIDEOPLUGIN_BACKGROUND_CHOICES', (
        [],
    )
)

COLOR_CHOICES = getattr(
    settings, 'VIDEOPLUGIN_COLOR_CHOICES', (
        [],
    )
)
