import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import (
    check_settings,
    get_baseplugin_fieldset,
)

# basics
NAME = _("PluginTemplate")
MODULE = defaults.CONTENT_LABEL

# parent / children
ALLOW_CHILDREN = False
CHILD_CLASSES = []
REQUIRE_PARENT = False

# fields
TRANSLATED_FIELDS = []
CONTENT_FIELDS = [
    "title",
]
DESIGN_FIELDS = [
    "layout",
]
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

# choices
LAYOUT_CHOICES = (
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

# check for django settings that override!
check_settings("PLUGINTEMPLATEPLUGIN", sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(
    **{
        "design": DESIGN_FIELDS,
        "content": CONTENT_FIELDS,
        "advanced": ADVANCED_FIELDS,
    }
)
