# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults


HTMLBLOCKPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'HTMLBLOCKPLUGIN_CONTENT_FIELDS', (
        'htmlblock',
    )
)

HTMLBLOCKPLUGIN_FIELDSETS = getattr(
    settings, 'HTMLBLOCKPLUGIN_FIELDSETS', (
        (_('content'), {
            'classes': ['section', 'content-section'],
            'fields': HTMLBLOCKPLUGIN_CONTENT_FIELDS,
        }),
        (_('advanced settings'), {
            'classes': ('section', 'settings-advanced'),
            'fields': defaults.BASEPLUGIN_ADVANCED_FIELDS,
        }),
    )
)
