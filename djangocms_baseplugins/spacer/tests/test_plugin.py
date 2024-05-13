from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.spacer.cms_plugins import SpacerPlugin


class SpacerPluginTests(BasePluginTestCase, TestCase):
    plugin_class = SpacerPlugin
    plugin_settings_prefix = "SPACERPLUGIN"
    plugin_path = "djangocms_baseplugins.spacer"
