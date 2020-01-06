from __future__ import unicode_literals

from django.test import TestCase
from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase

from ..cms_plugins import PlugintemplatePlugin


class PlugintemplatePluginTests(BasePluginTestCase, TestCase):
    plugin_class = PlugintemplatePlugin
    plugin_settings_prefix = 'PLUGINTEMPLATEPLUGIN'
