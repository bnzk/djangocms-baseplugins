from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.download.cms_plugins import DownloadPlugin, DownloadSectionPlugin


class DownloadSectionPluginTests(BasePluginTestCase, TestCase):
    plugin_class = DownloadSectionPlugin
    plugin_settings_prefix = 'DOWNLOADSECTIONPLUGIN'


class DownloadPluginTests(BasePluginTestCase, TestCase):
    plugin_class = DownloadPlugin
    plugin_settings_prefix = 'DOWNLOADPLUGIN'
