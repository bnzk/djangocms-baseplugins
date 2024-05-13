import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import (
    check_settings,
    get_baseplugin_fieldset,
)

# clean when saving? default is to clean on render AND save.
CLEAN_ON_SAVE = True

NAME = _("Text")

TRANSLATED_FIELDS = [
    "body",
]
DESIGN_FIELDS = []
CONTENT_FIELDS = [
    "body",
]
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

# check for django settings that override, also, not existing settings will be added
check_settings("TEXTPLUGIN", sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(
    **{
        "design": DESIGN_FIELDS,
        "content": CONTENT_FIELDS,
        "advanced": ADVANCED_FIELDS,
    }
)
