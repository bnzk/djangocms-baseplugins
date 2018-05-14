from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.twitter.cms_plugins import TweetEmbedPlugin


class TweetEmbedPluginTests(BasePluginTestCase, TestCase):

    plugin_class = TweetEmbedPlugin
    plugin_settings_prefix = 'TWEETEMBEDPLUGIN'

    def get_plugin_default_data(self):
        return {
            'tweet_url': 'https://twitter.com/MdDoomFest/status/795834590481018880',
        }