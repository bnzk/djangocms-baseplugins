import re
import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.defaults import ADVANCED_FIELDS
from djangocms_baseplugins.baseplugin.utils import (
    check_settings,
    get_baseplugin_fieldset,
)

NAME = _("Video")
MODULE = defaults.CONTENT_LABEL

TRANSLATED_FIELDS = [
    "video_url",
]

# thx to rouxcode!
REGEXES = (
    re.compile(r"^https?\:\/\/(www\.)?youtu\.be\/(?P<youtube_id>[^\/]*)\??.*$"),
    re.compile(
        r"^https?\:\/\/(www\.)?youtube\.(com|nl|ru).*v=(?P<youtube_id>.*)\&?.*$"
    ),
    re.compile(
        r"^https?\:\/\/(www\.)?youtube\.(com|nl|ru)\/embed\/(?P<youtube_id>[^\/]*)\??.*$"
    ),
    re.compile(r"^https?\:\/\/(www\.)?vimeo\.com\/(?P<vimeo_id>[^\/]*)\??.*$"),
)

YOUTUBE_MODESTBRANDING = True

YOUTUBE_COLOR = "red"  # or white
VIMEO_COLOR = False  # default blue

CONTENT_FIELDS = (
    "video_url",
    ("show_related", "autoplay", "mute", "controls", "infos", "fullscreen"),
)

DESIGN_FIELDS = []

LAYOUT_CHOICES = defaults.LAYOUT_CHOICES
BACKGROUND_CHOICES = defaults.BACKGROUND_CHOICES
COLOR_CHOICES = defaults.COLOR_CHOICES
SIZE_CHOICES = defaults.SIZE_CHOICES
CUSTOM_CHOICES = defaults.CUSTOM_CHOICES


# check for django settings that override!
check_settings("VIDEOPLUGIN", sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(
    **{
        "design": DESIGN_FIELDS,
        "content": CONTENT_FIELDS,
        "advanced": ADVANCED_FIELDS,
    }
)
