import sys

from django.conf import settings

from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


TRANSLATED_FIELDS = ['body', ]
CONTENT_FIELDS = [
    'website',
    'email',
    'phone',
    'address',
    'geocoding_address',
    'body',
]
DESIGN_FIELDS = []

CHILD_CLASSES = ('PersonSection', )


# check for django settings that override!
check_settings('CONTACTPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
