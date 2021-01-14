# import importlib
import importlib

from cms.plugin_pool import plugin_pool
from cms.api import add_plugin, create_page
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.test import RequestFactory, Client
from django.utils.encoding import force_text


class BasePluginTestCase(object):
    plugin_class = None  # TextPlugin
    plugin_settings_prefix = ''  # optional, 'TEXTPLUGIN'
    plugin_path = ''  # 'djangocms_baseplugins.text'
    additional_plugins = []

    def __init__(self, *args, **kwargs):
        if not self.plugin_settings_prefix:
            self.plugin_settings_prefix = self.plugin_class.__name__.upper()
        return super().__init__(*args, **kwargs)

    def setUp(self):
        # reload models (custom base plugin model!)
        abstract_models = importlib.import_module('djangocms_baseplugins.baseplugin.models')
        importlib.reload(abstract_models)
        # reload plugin conf/settings
        self._reload_plugins_settings()
        # prepare
        self.username = "test_admin"
        self.password = "testPW"
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user
        client = Client()
        client.login(username=self.username, password=self.password)

    def tearDown(self):
        pass

    def _reload_plugins_settings(self):
        """
        must reload plugins for every test, as changed settings can cause bad things.
        :return:
        """
        # is it ready for the reload?
        if not self.plugin_path:
            print(
                'not yet reloadable, add plugin_path to testcase for: {}'
                .format(self.plugin_class.__name__)
            )
        else:
            conf = importlib.import_module('{}.conf'.format(self.plugin_path))
            cms_plugins = importlib.import_module('{}.cms_plugins'.format(self.plugin_path))
            importlib.reload(conf)
            plugin_pool.unregister_plugin(self.plugin_class)
            for additional in self.additional_plugins:
                plugin_pool.unregister_plugin(additional)
            importlib.reload(cms_plugins)
            self.plugin_class = getattr(cms_plugins, self.plugin_class.__name__)

    def get_plugin_default_data(self):
        return {}

    def test_basic_admin_form(self):
        """
        just calling add plugin admin view
        like /admin/cms/page/add-plugin/?placeholder_id=43&plugin
        _type=SectionPlugin&cms_path=%2Fen%2F&plugin_language=en
        :return:
        """
        client = Client()
        client.login(username=self.username, password=self.password)
        page = create_page('test', 'base.html', 'en', slug='test', )
        placeholder = Placeholder.objects.create(page=page, slot='test')
        url = '/admin/cms/page/add-plugin/?' \
            + 'placeholder_id={}&plugin_type={}' \
            + '&cms_path=%2Fen%2F&plugin_language=en'
        url = url.format(placeholder.id, self.plugin_class.__name__)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    # not yet. reloading conf is not enough!?
    def test_basic_admin_form_choices_overrides(self):
        """
        just calling add plugin admin view, check if layout/background/color
        custom choices work
        :return:
        """
        if not getattr(self, 'plugin_path', None):
            return
        client = Client()
        client.login(username=self.username, password=self.password)
        page = create_page('test', 'base.html', 'en', slug='test', )
        placeholder = Placeholder.objects.create(page=page, slot='test')
        settings_kwargs = {
            '{}_LAYOUT_CHOICES'.format(self.plugin_settings_prefix): (('0000-layout', 'Nope'),),
            '{}_COLOR_CHOICES'.format(self.plugin_settings_prefix): (('0000-color', 'Nope'),),
            '{}_BACKGROUND_CHOICES'.format(self.plugin_settings_prefix): (('0000-background', 'Nope'),),  # noqa
            '{}_DESIGN_FIELDS'.format(self.plugin_settings_prefix): ('layout', 'color', 'background', ),  # noqa
            '{}_CONTENT_FIELDS'.format(self.plugin_settings_prefix): ('title', ),
        }
        with self.settings(**settings_kwargs):
            self._reload_plugins_settings()
            url = '/admin/cms/page/add-plugin/?' \
                + 'placeholder_id={}&plugin_type={}' \
                + '&cms_path=%2Fen%2F&plugin_language=en'
            url = url.format(placeholder.id, self.plugin_class.__name__)
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
            # print(response.status_code)
            self.assertContains(response, 'id_layout')
            self.assertContains(response, '0000-layout')
            self.assertContains(response, 'id_color')
            self.assertContains(response, '0000-color')
            self.assertContains(response, '0000-background')

    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            self.plugin_class,
            'en',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, placeholder)
        self.assertIn('object', context)

    def test_plugin_bem_classes_applied(self):
        """
        test if BEM style classes are applied to this plugins output
        :return:
        """
        placeholder = Placeholder.objects.create(slot='test')
        data = {
            'anchor': 'anchor-value',
            'layout': 'layout-value',
            'color': 'color-value',
            'background': 'background-value',
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
        plugin_name = model_instance.__class__.__name__.lower()
        self.assertIn('plugin_{}'.format(model_instance.pk), force_text(html))
        self.assertIn('plugin-{}'.format(plugin_name), force_text(html))
        self.assertIn('plugin-{}_{}'.format(plugin_name, 'layout-value'), force_text(html))
        self.assertIn('plugin-{}_{}'.format(plugin_name, 'color-value'), force_text(html))
        self.assertIn('plugin-{}_{}'.format(plugin_name, 'background-value'), force_text(html))
        self.assertIn('plugin-{}_anchor-{}'.format(plugin_name, 'anchor-value'), force_text(html))

    def test_translated_improperly_configured(self):
        return
        # settings_kwargs = {
        #     'DJANGOCMS_BASEPLUGINS_BASEMODEL': 'test_app.models.CustomAbstractBasePlugin',
        # }
        # with self.settings(**settings_kwargs):
        #     baseplugin_models = importlib.import_module('djangocms_baseplugins.image.models')
        #     importlib.reload(baseplugin_models)

    def test_custom_baseclass_improperly_configured(self):
        if getattr(self, 'plugin_path', None):
            settings_kwargs = {
                'DJANGOCMS_BASEPLUGINS_BASEMODEL': 'test_app.models.CustomAbstractBasePlugin',
            }
            with self.settings(**settings_kwargs):
                # check if our models raises, as we are not in MIGRATION_MODULES
                models_path = '{}.models'.format(self.plugin_path)
                baseplugin_models = importlib.import_module(models_path)
                # throws = False
                # try:
                #     importlib.reload(baseplugin_models)
                # except ImproperlyConfigured:
                #     throws = True
                # self.assertEqual(throws, True)
                # check message!
                with self.assertRaises(ImproperlyConfigured) as exception:
                    importlib.reload(baseplugin_models)
                exception_message = str(exception.exception)
                module_path, plugin_module_name = self.plugin_path.rsplit('.', 1)
                exception_part = '"{}" in settings.MIGRATION_MODULES'.format(plugin_module_name)
                self.assertEquals(True, exception_part in exception_message)

    def test_form_choices_and_other_settings_respected(self):
        """
        :return:
        """
        return
