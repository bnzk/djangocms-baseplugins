from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.slider.cms_plugins import SliderPlugin


class SliderPluginTests(BasePluginTestCase, TestCase):
    plugin_class = SliderPlugin
    plugin_settings_prefix = 'SLIDERPLUGIN'
    plugin_path = 'djangocms_baseplugins.slider'
