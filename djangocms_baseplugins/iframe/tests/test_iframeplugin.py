from __future__ import unicode_literals

from django.test import TestCase
from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase

from ..cms_plugins import IframePlugin


class IframePluginTests(BasePluginTestCase, TestCase):
    plugin_class = IframePlugin
    plugin_path = 'djangocms_baseplugins.iframe'
    plugin_settings_prefix = 'IFRAMEPLUGIN'
