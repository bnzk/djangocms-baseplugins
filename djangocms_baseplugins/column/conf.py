import sys

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset, check_settings

TRANSLATED_FIELDS = []
CONTENT_FIELDS = []
DESIGN_FIELDS = []
ADVANCED_FIELDS = defaults.ADVANCED_FIELDS

WIDTH_CHOICES = defaults.WIDTH_CHOICES

CHILD_CLASSES = (
        'TextPlugin',
        'TextImagePlugin',
        'ImagePlugin',
        'VideoPlugin',
        'TweetEmbedPlugin',
        'HtmlBlockPlugin',
    )

ALLOW_CHILDREN = True

LAYOUT_CHOICES = (
    ('2whatwhat', _("2 Spalten"),),
    ('3', _("3 Spalten"),),
    ('4', _("4 Spalten"),),
)
BACKGROUND_CHOICES = (
    ('white', _("Weiss"),),
    ('beige', _("Beige"),),
    ('grey', _("Grau"),),
)
COLOR_CHOICES = (
    ('default', _("Default"),),
)
SIZE_CHOICES = (
    ('default', _("Default"),),
)
CUSTOM_CHOICES = (
    ('default', _("Default"),),
)


# check for django settings that override!
check_settings('COLUMNPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})
