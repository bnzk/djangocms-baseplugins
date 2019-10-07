from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.contact.cms_plugins import ContactPlugin


class AutoColumnsPluginTests(BasePluginTestCase, TestCase):
    plugin_class = ContactPlugin
    plugin_settings_prefix = 'AUTOCOLUMNSPLUGIN'
