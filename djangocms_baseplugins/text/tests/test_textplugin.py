from __future__ import unicode_literals

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.test import TestCase
from django.test.client import RequestFactory
from django.utils.encoding import force_str

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.text.cms_plugins import TextPlugin


class TextPluginTests(BasePluginTestCase, TestCase):
    plugin_class = TextPlugin
    plugin_settings_prefix = "TEXTPLUGIN"
    plugin_path = "djangocms_baseplugins.text"

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot="test")
        model_instance = add_plugin(
            placeholder,
            self.plugin_class,
            "en",
            **{
                "body": "<strong>Test</strong>",
            }
        )
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})
        self.assertInHTML("<strong>Test</strong>", force_str(html))
