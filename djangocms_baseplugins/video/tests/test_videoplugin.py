from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import RequestFactory
from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.video.cms_plugins import VideoPlugin


class VideoPluginTests(BasePluginTestCase, TestCase):

    plugin_class = VideoPlugin
    plugin_settings_prefix = 'VIDEOPLUGIN'
