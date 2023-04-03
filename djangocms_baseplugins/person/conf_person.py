import sys

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


TRANSLATED_FIELDS = ['salutation', 'function', 'department', 'body', ]

DESIGN_FIELDS = []
CONTENT_FIELDS = [
    'image',
    ('title', 'function', 'department',),
    ('salutation', 'first_name', 'last_name',),
    'body',
    'email',
    'phone',
    'website',
]
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

ALLOW_CHILDREN = False
REQUIRE_PARENT = True

# check for django settings that override!
check_settings('PERSONPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
