from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.contentnav.cms_plugins import ContentNavPlugin


class ContentNavPluginTests(BasePluginTestCase, TestCase):
    plugin_class = ContentNavPlugin
    plugin_settings_prefix = 'CONTENTNAVPLUGIN'
    plugin_path = 'djangocms_baseplugins.contentnav'
