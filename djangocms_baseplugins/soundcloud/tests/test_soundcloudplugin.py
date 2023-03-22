from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from ..cms_plugins import SoundcloudPlugin


class SoundcloudPluginTests(BasePluginTestCase, TestCase):
    plugin_class = SoundcloudPlugin
    plugin_path = 'djangocms_baseplugins.soundcloud'

    def get_plugin_default_data(self):
        return {
            'soundcloud_url': 'https://soundcloud.com/grappainc/sinatras-movenr137?',
        }
