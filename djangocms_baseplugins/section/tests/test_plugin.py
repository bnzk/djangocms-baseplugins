from __future__ import unicode_literals

from django.test import TestCase

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.section.cms_plugins import SectionPlugin


class SectionPluginTests(BasePluginTestCase, TestCase):
    plugin_class = SectionPlugin
    plugin_settings_prefix = 'SECTIONPLUGIN'
    plugin_path = 'djangocms_baseplugins.section'

    # def test_section_plugin_special_classes_applied(self):
    #     """
    #     test if BEM style classes are applied to this plugins output
    #     :return:
    #     """
    #     placeholder = Placeholder.objects.create(slot='test')
    #     data = {
    #         'width': 'w-33',
    #     }
    #     data.update(self.get_plugin_default_data())
    #     model_instance = add_plugin(
    #         placeholder,
    #         self.plugin_class,
    #         'en',
    #         **data
    #     )
    #     renderer = ContentRenderer(request=RequestFactory())
    #     html = renderer.render_plugin(model_instance, {})
    #     plugin_name = model_instance.__class__.__name__.lower()
    #     self.assertIn('plugin-column_{}'.format(model_instance.width), force_text(html))
