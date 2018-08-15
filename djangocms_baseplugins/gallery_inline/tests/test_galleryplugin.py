from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.gallery.cms_plugins import GalleryPlugin


class GalleryPluginTests(BasePluginTestCase, TestCase):

    plugin_class = GalleryPlugin
    plugin_settings_prefix = 'GALLERYPLUGIN'
