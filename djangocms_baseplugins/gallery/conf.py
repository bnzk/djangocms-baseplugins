import sys

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


NAME = _("Gallery")
MODULE = defaults.CONTAINER_LABEL

TRANSLATED_FIELDS = ['description', ]
DESIGN_FIELDS = []
CONTENT_FIELDS = []
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

ALLOW_CHILDREN = True
CHILD_CLASSES = (
    'ImagePlugin',
    'TextImagePlugin',
)


# check for django settings that override!
check_settings('GALLERYPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
