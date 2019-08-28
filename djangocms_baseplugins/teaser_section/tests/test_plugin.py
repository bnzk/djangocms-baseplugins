from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.teaser_section.cms_plugins import TeaserSectionPlugin


class TeaserSectionPluginTests(BasePluginTestCase, TestCase):
    plugin_class = TeaserSectionPlugin
    plugin_settings_prefix = 'TEASERSECTIONPLUGIN'
