from __future__ import unicode_literals

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.test import TestCase, RequestFactory
from django.utils.encoding import force_text

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.column.cms_plugins import ColumnPlugin


class ColumnPluginTests(BasePluginTestCase, TestCase):
    plugin_class = ColumnPlugin
    plugin_settings_prefix = 'COLUMNPLUGIN'

    def test_plugin_special_classes_applied(self):
        """
        test if BEM style classes are applied to this plugins output
        :return:
        """
        placeholder = Placeholder.objects.create(slot='test')
        data = {
            'width': 'w-33',
        }
        data.update(self.get_plugin_default_data())
        model_instance = add_plugin(
            placeholder,
            self.plugin_class,
            'en',
            **data
        )
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})
        # plugin_name = model_instance.__class__.__name__.lower()
        self.assertIn(
            'plugin-column_{}'.format(model_instance.width),
            force_text(html)
        )
