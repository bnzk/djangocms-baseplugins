from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.column.cms_plugins import ColumnPlugin


class ColumnPluginTests(BasePluginTestCase, TestCase):

    plugin_class = ColumnPlugin
    plugin_settings_prefix = 'COLUMNPLUGIN'
