from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.video.cms_plugins import VideoPlugin


class VideoPluginTests(BasePluginTestCase, TestCase):
    plugin_class = VideoPlugin
    plugin_settings_prefix = 'VIDEOPLUGIN'
