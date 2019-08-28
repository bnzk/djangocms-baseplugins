from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.image.cms_plugins import ImagePlugin


class ImagePluginTests(BasePluginTestCase, TestCase):
    plugin_class = ImagePlugin
    plugin_settings_prefix = 'IMAGEPLUGIN'
