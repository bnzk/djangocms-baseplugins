from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from ..cms_plugins import FormDesignerPlugin


class FormDesignerPluginTests(BasePluginTestCase, TestCase):
    plugin_class = FormDesignerPlugin
    plugin_path = 'djangocms_baseplugins.cms_form_designer'
