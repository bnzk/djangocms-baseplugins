from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.section.cms_plugins import SectionPlugin


class SectionPluginTests(BasePluginTestCase, TestCase):

    plugin_class = SectionPlugin
    plugin_settings_prefix = 'SECTIONPLUGIN'
