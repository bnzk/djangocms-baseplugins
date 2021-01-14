# import importlib
import importlib

from cms.plugin_pool import plugin_pool
from cms.api import add_plugin, create_page
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.test import RequestFactory, Client, TestCase
from django.utils.encoding import force_text


class ConfigurationTestCase(TestCase):

    def setUp(self):
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
        pass
        # is it ready for the reload?
        # conf = importlib.import_module('{}.conf'.format(self.plugin_path))
        # cms_plugins = importlib.import_module('{}.cms_plugins'.format(self.plugin_path))
        # importlib.reload(conf)
        # plugin_pool.unregister_plugin(self.plugin_class)
        # for additional in self.additional_plugins:
        #     plugin_pool.unregister_plugin(additional)
        # importlib.reload(cms_plugins)
        # self.plugin_class = getattr(cms_plugins, self.plugin_class.__name__)

    def get_plugin_default_data(self):
        return {}

    def test_invalid_custom_baseclass_improperly_configured(self):
        settings_kwargs = {
            'DJANGOCMS_BASEPLUGINS_BASEMODEL': 'test_app.models.InvalidAbstractBasePlugin',
        }
        with self.settings(**settings_kwargs):
            baseplugin_models = importlib.import_module('djangocms_baseplugins.baseplugin.models')
            throws = False
            try:
                importlib.reload(baseplugin_models)
            except ImproperlyConfigured:
                throws = True
            self.assertEqual(throws, True)

    def test_not_existing_custom_baseclass_improperly_configured(self):
        settings_kwargs = {
            'DJANGOCMS_BASEPLUGINS_BASEMODEL': 'test_app.models.ObjectNotThereAbstractBasePlugin',
        }
        with self.settings(**settings_kwargs):
            baseplugin_models = importlib.import_module('djangocms_baseplugins.baseplugin.models')
            throws = False
            try:
                importlib.reload(baseplugin_models)
            except ImproperlyConfigured:
                throws = True
            self.assertEqual(throws, True)

