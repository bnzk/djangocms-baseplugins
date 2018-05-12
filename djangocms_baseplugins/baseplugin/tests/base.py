from cms.api import add_plugin
from cms.models import Placeholder


class BasePluginTestCase(object):

    plugin_class = None  # TextPlugin
    plugin_settings_prefix = ''  # TEXTPLUGIN

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
