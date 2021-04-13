from django.test import TestCase
from form_designer.models import Form

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from ..cms_plugins import FormDesignerPlugin


class FormDesignerPluginTests(BasePluginTestCase, TestCase):
    plugin_class = FormDesignerPlugin
    plugin_path = 'djangocms_baseplugins.cms_form_designer'

    def setUp(self):
        super().setUp()
        self.form = Form()
        self.form.save()

    def get_plugin_default_data(self):
        return {
            'form': self.form,
            'title': 'TestFormPlugin',
        }
