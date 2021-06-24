import re
import sys

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.defaults import ADVANCED_FIELDS
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset, check_settings

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
LAYOUT_CHOICES = defaults.LAYOUT_CHOICES
BACKGROUND_CHOICES = defaults.BACKGROUND_CHOICES
COLOR_CHOICES = defaults.COLOR_CHOICES
SIZE_CHOICES = defaults.SIZE_CHOICES
CUSTOM_CHOICES = defaults.CUSTOM_CHOICES


# check for django settings that override!
check_settings('VIDEOPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
