from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.download.cms_plugins import DownloadPlugin, DownloadSectionPlugin


class DownloadSectionPluginTests(BasePluginTestCase, TestCase):
    plugin_path = 'djangocms_baseplugins.download'
    plugin_class = DownloadSectionPlugin
    plugin_conf = 'conf_section'
    additional_plugins = [DownloadPlugin, ]


class DownloadPluginTests(BasePluginTestCase, TestCase):
    plugin_path = 'djangocms_baseplugins.download'
    plugin_class = DownloadPlugin
    plugin_conf = 'conf_entry'
    additional_plugins = [DownloadSectionPlugin, ]
