import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import (
    check_settings,
    get_baseplugin_fieldset,
)

# basics
NAME = _("Login Form")
MODULE = defaults.ADVANCED_LABEL

# parent / children
ALLOW_CHILDREN = False
CHILD_CLASSES = []
REQUIRE_PARENT = False

TRANSLATED_FIELDS = []
DESIGN_FIELDS = []
CONTENT_FIELDS = []
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
SIZE_CHOICES = (
    (
        "default",
        _("Default"),
    ),
)
BACKGROUND_CHOICES = (
    (
        "default",
        _("Default"),
    ),
)
COLOR_CHOICES = (
    (
        "default",
        _("Default"),
    ),
)
CUSTOM_CHOICES = (
    (
        "default",
        _("Default"),
    ),
)

# check for django settings that override!
check_settings("LOGINFORMPLUGIN", sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(
    **{
        "design": DESIGN_FIELDS,
        "content": CONTENT_FIELDS,
        "advanced": ADVANCED_FIELDS,
    }
)
