# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults


TWEETEMBEDPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'TWEETEMBEDPLUGIN_CONTENT_FIELDS', (
        'tweet_url',
    )
)

TWEETEMBEDPLUGIN_FIELDSETS = getattr(
    settings, 'TWEETEMBEDPLUGIN_FIELDSETS', (
        (_('content'), {
            'classes': ['section', 'content-section'],
            'fields': TWEETEMBEDPLUGIN_CONTENT_FIELDS,
        }),
        (_('advanced settings'), {
            'classes': ('section', 'settings-advanced'),
            'fields': defaults.BASEPLUGIN_ADVANCED_FIELDS,
        }),
    )
)
