# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TWEETEMBEDPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'TWEETEMBEDPLUGIN_TRANSLATED_FIELDS', [
        'tweet_url',
    ]
)

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
    get_baseplugin_fieldset(**{
        'design': TWEETEMBEDPLUGIN_DESIGN_FIELDS,
        'content': TWEETEMBEDPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.ADVANCED_FIELDS,
    })
)

TWEETEMBEDPLUGIN_LAYOUT_CHOICES = getattr(
    settings,
    'TWEETEMBEDPLUGIN_LAYOUT_CHOICES',
    (
        ('default', _("Default"),),
    )
)

TWEETEMBEDPLUGIN_BACKGROUND_CHOICES = getattr(
    settings,
    'TWEETEMBEDPLUGIN_BACKGROUND_CHOICES',
    (
        ('default', _("Default"),),
    )
)

TWEETEMBEDPLUGIN_COLOR_CHOICES = getattr(
    settings,
    'TWEETEMBEDPLUGIN_COLOR_CHOICES',
    (
        ('default', _("Default"),),
    )
)
