from __future__ import unicode_literals

from django.test import TestCase
from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase

from ..cms_plugins import PluginTemplatePlugin


class PluginTemplatePluginTests(BasePluginTestCase, TestCase):
    plugin_class = PluginTemplatePlugin
    plugin_settings_prefix = 'PLUGINTEMPLATEPLUGIN'
