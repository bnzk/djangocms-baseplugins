from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_TRANSLATED_FIELDS', []
)

CONTENT_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_CONTENT_FIELDS', []
)

DESIGN_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_DESIGN_FIELDS', []
)

FIELDSETS = getattr(
    settings,
    'TEASERSECTIONPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

CHILD_CLASSES = getattr(
    settings, 'TEASERSECTIONPLUGIN_CHILD_CLASSES', (
        'TextImagePlugin',
        # or your own, custom teaser plugin
    )
)

LAYOUT_CHOICES = getattr(
    settings,
    'TEASERSECTIONPLUGIN_LAYOUT_CHOICES',
    (
        ('2', _("2 Spalten"),),
        ('3', _("3 Spalten"),),
        ('4', _("4 Spalten"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'TEASERSECTIONPLUGIN_BACKGROUND_CHOICES',
    (
        ('white', _("Weiss"),),
        ('beige', _("Beige"),),
        ('grey', _("Grau"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'TEASERSECTIONPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
