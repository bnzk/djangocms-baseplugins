import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import (
    check_settings,
    get_baseplugin_fieldset,
)

# basics
NAME = _("Iframe")
MODULE = defaults.CONTENT_LABEL

# parent / children
ALLOW_CHILDREN = False
CHILD_CLASSES = []
REQUIRE_PARENT = False

TRANSLATED_FIELDS = []
CONTENT_FIELDS = [
    "iframe_url",
]
DESIGN_FIELDS = [
    "layout",
]
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

LAYOUT_CHOICES = (
    (
        "full",
        _("Full Size"),
    ),
    (
        "content",
        _("Content Sized"),
    ),
)


# check for django settings that override!
check_settings("IFRAMEPLUGIN", sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(
    **{
        "design": DESIGN_FIELDS,
        "content": CONTENT_FIELDS,
        "advanced": ADVANCED_FIELDS,
    }
)
