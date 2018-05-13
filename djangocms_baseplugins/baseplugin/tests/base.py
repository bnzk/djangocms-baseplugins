from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.test import RequestFactory
from django.utils.encoding import force_text


class BasePluginTestCase(object):

    plugin_class = None  # TextPlugin
    plugin_settings_prefix = ''  # TEXTPLUGIN

    def test_basic_admin_form(self):
        """
        just calling add plugin admin view
        like /admin/cms/page/add-plugin/?placeholder_id=43&plugin_type=SectionPlugin&cms_path=%2Fen%2F&plugin_language=en
        :return:
        """
        return

    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            self.plugin_class,
            'en',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('object', context)

    def test_plugin_bem_classes_applied(self):
        """
        test if BEM style classes are applied to this plugins output
        :return:
        """
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            self.plugin_class,
            'en',
            **{
                'layout': 'layout-value',
                'color': 'color-value',
                'background': 'background-value',
            }
        )
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})
        plugin_name = model_instance.__class__.__name__.lower()
        self.assertIn('plugin_{}'.format(model_instance.pk), force_text(html))
        self.assertIn('plugin-{}'.format(plugin_name), force_text(html))
        self.assertIn('plugin-{}_{}'.format(plugin_name, 'layout-value'), force_text(html))
        self.assertIn('plugin-{}_{}'.format(plugin_name, 'color-value'), force_text(html))
        self.assertIn('plugin-{}_{}'.format(plugin_name, 'background-value'), force_text(html))

    def test_form_choices_and_other_settings_respected(self):
        """
        :return:
        """
        return
