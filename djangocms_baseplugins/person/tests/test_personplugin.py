from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.person.cms_plugins import PersonPlugin, PersonSectionPlugin


class PersonPluginTests(BasePluginTestCase, TestCase):
    plugin_class = PersonPlugin
    plugin_path = 'djangocms_baseplugins.person'
    plugin_settings_prefix = 'PERSONPLUGIN'
    additional_plugins = [PersonSectionPlugin, ]


class PersonSectionPluginTests(BasePluginTestCase, TestCase):
    plugin_class = PersonSectionPlugin
    plugin_path = 'djangocms_baseplugins.person'
    plugin_settings_prefix = 'PERSONSECTIONPLUGIN'
    additional_plugins = [PersonPlugin, ]
