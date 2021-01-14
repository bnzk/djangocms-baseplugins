from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TRANSLATED_FIELDS = getattr(
    settings, 'SECTIONPLUGIN_TRANSLATED_FIELDS', []
)

CONTENT_FIELDS = getattr(
    settings, 'SECTIONPLUGIN_CONTENT_FIELDS', []
)

DESIGN_FIELDS = getattr(
    settings, 'SECTIONPLUGIN_DESIGN_FIELDS', []
)

FIELDSETS = getattr(
    settings,
    'SECTIONPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

CHILD_CLASSES = getattr(
    settings, 'SECTIONPLUGIN_CHILD_CLASSES', (
        'ColumnPlugin',
    )
)

LAYOUT_CHOICES = getattr(
    settings,
    'SECTIONPLUGIN_LAYOUT_CHOICES',
    (
        ('default', _("Default"),),
    )
)

BACKGROUND_CHOICES = getattr(
    settings,
    'SECTIONPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

COLOR_CHOICES = getattr(
    settings,
    'SECTIONPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
