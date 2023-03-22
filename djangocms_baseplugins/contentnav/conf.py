import sys

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_settings, get_baseplugin_fieldset


TRANSLATED_FIELDS = []
CONTENT_FIELDS = ['menu_depth', 'cms_page', 'sitemap', ],
DESIGN_FIELDS = []
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS


# check for django settings that override!
check_settings('CONTENTNAVPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
