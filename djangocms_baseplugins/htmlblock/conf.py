import sys

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset, check_settings


# basics
NAME = _('HTML Block')
MODULE = defaults.ADVANCED_LABEL

# parent / children
ALLOW_CHILDREN = True
CHILD_CLASSES = [
    'TextPlugin',
    'TextImagePlugin',
]
REQUIRE_PARENT = False

# fields
TRANSLATED_FIELDS = ['htmlblock', ]
CONTENT_FIELDS = ['htmlblock']
DESIGN_FIELDS = ['layout', ]

# choices
LAYOUT_CHOICES = (
    ('full', _("Full Size"),),
    ('content', _("Content Sized"),),
)


# check for django settings that override!
check_settings('HTMLBLOCKPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
