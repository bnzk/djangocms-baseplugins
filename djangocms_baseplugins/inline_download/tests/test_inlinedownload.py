from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.inline_download.cms_plugins import InlineDownloadPlugin


class InlineDownloadPluginTests(BasePluginTestCase, TestCase):
    plugin_class = InlineDownloadPlugin
    plugin_path = 'djangocms_baseplugins.inline_download'
