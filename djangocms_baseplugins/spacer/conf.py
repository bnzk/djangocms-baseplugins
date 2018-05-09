# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


SPACERPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'SPACERPLUGIN_CONTENT_FIELDS', [])

SPACERPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'SPACERPLUGIN_DESIGN_FIELDS', ['layout'])

SPACERPLUGIN_FIELDSETS = getattr(
    settings,
    'SPACERPLUGIN_FIELDSETS ',
    build_baseplugin_fieldset(**{
        'content': SPACERPLUGIN_CONTENT_FIELDS,
        'design': SPACERPLUGIN_DESIGN_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

SPACERPLUGIN_LAYOUT_CHOICES = getattr(
    settings, 'SPACERPLUGIN_LAYOUT_CHOICES', (
        ('', _("-")),
        ('remove-all-space', _("Remove space")),
        ('remove-half-space', _("Remove half space")),
        ('add-some-more-space', _("Add little more space")),
        ('add-more-space', _("Add more space")),
    )
)
