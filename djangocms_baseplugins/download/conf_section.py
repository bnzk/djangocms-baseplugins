import sys

from django.conf import settings

from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


DOWNLOADSECTIONPLUGIN_TRANSLATED_FIELDS = []

ALLOW_CHILDREN = True
CHILD_CLASSES = ('DownloadPlugin', )


# check for django settings that override!
check_settings('DOWNLOADSECTIONPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})

