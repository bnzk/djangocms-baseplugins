from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from ..cms_plugins import SoundcloudPlugin


class AutoColumnsPluginTests(BasePluginTestCase, TestCase):
    plugin_class = SoundcloudPlugin
    plugin_path = 'djangocms_baseplugins.soundcloud'
