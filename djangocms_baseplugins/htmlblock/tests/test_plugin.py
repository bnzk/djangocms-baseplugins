from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.htmlblock.cms_plugins import HtmlBlockPlugin


class HtmlBlockPluginTests(BasePluginTestCase, TestCase):
    plugin_class = HtmlBlockPlugin
    plugin_settings_prefix = 'HTMLBLOCKPLUGIN'

    def get_plugin_default_data(self):
        return {
            'htmlblock': '<div></div>'
        }
