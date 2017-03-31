# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults


COLUMNPLUGIN_FIELDSETS = getattr(
    settings, 'COLUMNPLUGIN_FIELDSETS ', (
        (_('advanced settings'), {
            'classes': ('section', 'settings-advanced'),
            'fields': defaults.BASEPLUGIN_ADVANCED_FIELDS,
        }),
    )
)

COLUMNPLUGIN_WIDTH_CHOICES = getattr(
    settings, 'COLUMNPLUGIN_WIDTH_CHOICES', (
        defaults.WIDTH_CHOICES
    )
)

COLUMNPLUGIN_CHILD_CLASSES = getattr(
    settings, 'COLUMNPLUGIN_CHILD_CLASSES', (
        'TextPlugin',
        'ImagePlugin',
        'VideoPlugin',
    )
)
