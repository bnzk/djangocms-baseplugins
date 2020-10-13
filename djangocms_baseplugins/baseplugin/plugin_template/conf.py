# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset


# basics
NAME = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_NAME', _('PluginTemplate')
)
MODULE = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_MODULE', defaults.CONTENT_LABEL,
)


# parent / children
ALLOW_CHILDREN = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_ALLOW_CHILDREN', False
)
CHILD_CLASSES = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_CHILD_CLASSES', [
        'TextPlugin',
        'TextImagePlugin',
    ]
)
REQUIRE_PARENT = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_REQUIRE_PARENT', False
)


# fields
TRANSLATED_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_TRANSLATED_FIELDS', [
        'caption',
    ]
)
CONTENT_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_CONTENT_FIELDS', [
        'image',
        'caption',
    ]
)
DESIGN_FIELDS = getattr(
    settings, 'PLUGINTEMPLATEPLUGIN_DESIGN_FIELDS', [
        'layout',
    ]
)
FIELDSETS = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': DESIGN_FIELDS,
        'content': CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)


# choices
LAYOUT_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_LAYOUT_CHOICES',
    (
        ('full', _("Full Size"),),
        ('content', _("Content Sized"),),
    )
)
BACKGROUND_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_BACKGROUND_CHOICES',
    (
        ('white', _("Weiss"),),
        ('beige', _("Beige"),),
        ('grey', _("Grau"),),
    )
)
COLOR_CHOICES = getattr(
    settings,
    'PLUGINTEMPLATEPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
