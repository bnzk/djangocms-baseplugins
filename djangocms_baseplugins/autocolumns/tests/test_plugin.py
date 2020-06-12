from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from ..cms_plugins import AutoColumnsPlugin


class AutoColumnsPluginTests(BasePluginTestCase, TestCase):
    plugin_class = AutoColumnsPlugin
    plugin_path = 'djangocms_baseplugins.autocolumns'
