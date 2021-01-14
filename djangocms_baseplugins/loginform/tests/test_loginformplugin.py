from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.loginform.cms_plugins import LoginFormPlugin


class LoginFormPluginTests(BasePluginTestCase, TestCase):
    """
    TODO: find a solution for not working tests below (as request is passed as {}, it doesnt...
    """
    plugin_class = LoginFormPlugin
    plugin_path = 'djangocms_baseplugins.loginform'
    plugin_settings_prefix = 'LOGINFORMPLUGIN'

    def test_plugin_context(self):
        return

    def test_plugin_bem_classes_applied(self):
        return
