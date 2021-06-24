import sys

from django.conf import settings

from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


# clean when saving? default is to clean on render AND save.
CLEAN_ON_SAVE = True

TRANSLATED_FIELDS = ['body', ]


# check for django settings that override!
check_settings('TEXTPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
