from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


# clean when saving? default is to clean on render AND save.
CLEAN_ON_SAVE = getattr(
    settings,
    'TEXTPLUGIN_CLEAN_ON_SAVE',
    True,
)

TRANSLATED_FIELDS = getattr(
    settings, 'TEXTPLUGIN_TRANSLATED_FIELDS', [
        'body',
    ]
)

LAYOUT_CHOICES = getattr(
    settings, 'TEXTPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

BACKGROUND_CHOICES = getattr(
    settings, 'TEXTPLUGIN_BACKGROUND_CHOICES', (
        [],
    )
)

COLOR_CHOICES = getattr(
    settings, 'TEXTPLUGIN_COLOR_CHOICES', (
        [],
    )
)

CONTENT_FIELDS = getattr(
    settings, 'TEXTPLUGIN_CONTENT_FIELDS', (
        'body',
    )
)

DESIGN_FIELDS = getattr(
    settings, 'TEXTPLUGIN_DESIGN_FIELDS', []
)

FIELDSETS = getattr(
    settings,
    'TEXTPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

REQUIRE_PARENT = getattr(
    settings,
    'TEXTPLUGIN_REQUIRE_PARENT',
    False,
)
