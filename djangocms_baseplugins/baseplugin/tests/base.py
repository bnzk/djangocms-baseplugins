from cms.api import add_plugin, create_page
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.contrib.auth.models import User
from django.test import RequestFactory, Client
from django.utils.encoding import force_text


class BasePluginTestCase(object):

    plugin_class = None  # TextPlugin
    plugin_settings_prefix = ''  # TEXTPLUGIN

    def setUp(self):
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

    def get_plugin_default_data(self):
        return {}

    def test_basic_admin_form(self):
        """
        just calling add plugin admin view
        like /admin/cms/page/add-plugin/?placeholder_id=43&plugin_type=SectionPlugin&cms_path=%2Fen%2F&plugin_language=en
        :return:
        """
        client = Client()
        client.login(username=self.username, password=self.password)
        page = create_page('test', 'base.html', 'en', slug='test', )
        placeholder = Placeholder.objects.create(page=page, slot='test')
        url = '/admin/cms/page/add-plugin/?' \
            + 'placeholder_id={}&plugin_type={}&cms_path=%2Fen%2F&plugin_language=en'\
            .format(placeholder.id, self.plugin_class.__name__)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

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

    def test_form_choices_and_other_settings_respected(self):
        """
        :return:
        """
        return
