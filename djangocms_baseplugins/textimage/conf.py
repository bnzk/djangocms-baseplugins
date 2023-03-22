import sys

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


NAME = _(u'Text & Image')

CLEAN_ON_SAVE = True,
TRANSLATED_FIELDS = ['caption', 'body', ]
DESIGN_FIELDS = []
CONTENT_FIELDS = ('image', 'caption', 'body', )
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS
IMAGE_REQUIRED = True


# check for django settings that override!
check_settings('TEXTIMAGEPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
