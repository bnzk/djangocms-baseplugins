from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.inline_gallery.cms_plugins import InlineGalleryPlugin


class InlineGalleryPluginTests(BasePluginTestCase, TestCase):
    plugin_class = InlineGalleryPlugin
    plugin_path = 'djangocms_baseplugins.inline_gallery'
    plugin_settings_prefix = 'INLINEGALLERYPLUGIN'
