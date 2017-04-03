# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


TWEETEMBEDPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'TWEETEMBEDPLUGIN_CONTENT_FIELDS', (
        'tweet_url',
    )
)

TWEETEMBEDPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'TWEETEMBEDPLUGIN_DESIGN_FIELDS', []
)

TWEETEMBEDPLUGIN_FIELDSETS = getattr(
    settings,
    'TWEETEMBEDPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': TWEETEMBEDPLUGIN_DESIGN_FIELDS,
        'content': TWEETEMBEDPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)
