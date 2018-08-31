from __future__ import unicode_literals

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.test import TestCase, RequestFactory
from django.utils.encoding import force_text

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.contentnav.cms_plugins import ContentNavPlugin


class ContentNavPluginTests(BasePluginTestCase, TestCase):

    plugin_class = ContentNavPlugin
    plugin_settings_prefix = 'CONTENTNAVPLUGIN'
