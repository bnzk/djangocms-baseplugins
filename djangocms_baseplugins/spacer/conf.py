import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


NAME = _("Spacer")

TRANSLATED_FIELDS = []
DESIGN_FIELDS = ['layout']
CONTENT_FIELDS = []
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS
LAYOUT_CHOICES = getattr(
    settings, 'SPACERPLUGIN_LAYOUT_CHOICES', (
        ('remove-one', _("Remove space")),
        ('remove-half', _("Remove half space")),
        ('', ("-")),
        ('add-half', _("Add half space")),
        ('add-one', _("Add space")),
        ('add-double', _("Add double space")),
        ('add-triple', _("Add triple space")),
        # orig
        # ('remove-all-space', _("Remove space")),
        # ('remove-half-space', _("Remove half space")),
        # ('add-some-more-space', _("Add little more space")),
        # ('add-normal-space', _("Add normal space")),
        # ('add-double-normal-space', _("Add double of normal space")),
        # ('add-triple-normal-space', _("Add triple of normal space")),
    )
)


# check for django settings that override!
check_settings('SPACERPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
