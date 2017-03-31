# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults


IMAGEPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption',
    )
)

IMAGEPLUGIN_FIELDSETS = getattr(
    settings, 'IMAGEPLUGIN_FIELDSETS', (
        (_('content'), {
            'classes': ['section', 'content-section'],
            'fields': IMAGEPLUGIN_CONTENT_FIELDS,
        }),
        (_('advanced settings'), {
            'classes': ('section', 'settings-advanced'),
            'fields': defaults.BASEPLUGIN_ADVANCED_FIELDS,
        }),
    )
)
