import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import (
    check_settings,
    get_baseplugin_fieldset,
)

# basics
NAME = _("Auto Columns")
MODULE = defaults.CONTAINER_LABEL

# parent / children
ALLOW_CHILDREN = True
CHILD_CLASSES = [
    "TextPlugin",
    "TextImagePlugin",
]
REQUIRE_PARENT = False

# fields
TRANSLATED_FIELDS = []
CONTENT_FIELDS = []
DESIGN_FIELDS = [
    "layout",
]
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

# choices
LAYOUT_CHOICES = (
    (
        "2",
        _("2 Spalten"),
    ),
    (
        "3",
        _("3 Spalten"),
    ),
    (
        "4",
        _("4 Spalten"),
    ),
)
BACKGROUND_CHOICES = (
    (
        "white",
        _("Weiss"),
    ),
    (
        "beige",
        _("Beige"),
    ),
    (
        "grey",
        _("Grau"),
    ),
)
COLOR_CHOICES = (
    (
        "default",
        _("Default"),
    ),
)
SIZE_CHOICES = (
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
check_settings("AUTOCOLUMNSPLUGIN", sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(
    **{
        "design": DESIGN_FIELDS,
        "content": CONTENT_FIELDS,
        "advanced": ADVANCED_FIELDS,
    }
)
