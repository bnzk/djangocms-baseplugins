from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.textimage.cms_plugins import TextImagePlugin


class TextImagePluginTests(BasePluginTestCase, TestCase):
    plugin_class = TextImagePlugin
    plugin_settings_prefix = 'TEXTIMAGEPLUGIN'
