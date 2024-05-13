import importlib

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .default_model import DefaultAbstractBasePlugin

if getattr(settings, "DJANGOCMS_BASEPLUGINS_BASEMODEL", None):
    try:
        module_name, class_name = settings.DJANGOCMS_BASEPLUGINS_BASEMODEL.rsplit(
            ".", 1
        )
        module = importlib.import_module(module_name)
        my_class = getattr(module, class_name)
        AbstractBasePlugin = my_class
    except (ImportError, ValueError, AttributeError):
        # import error
        raise ImproperlyConfigured(
            'Could not import "{}" that is defined in '
            "settings.DJANGOCMS_BASEPLUGINS_BASEMODEL!".format(
                settings.DJANGOCMS_BASEPLUGINS_BASEMODEL
            )
        )
    # baseclass must still be DefaultAbstractBasePlugin
    if not issubclass(AbstractBasePlugin, DefaultAbstractBasePlugin):
        raise ImproperlyConfigured(
            "Your custom BasePlugin Model ({}) must inherit from"
            "djangocms_baseplugins.baseplugin.default_model.DefaultAbstractBasePlugin".format(  # noqa
                settings.DJANGOCMS_BASEPLUGINS_BASEMODEL
            )
        )
else:

    class AbstractBasePlugin(DefaultAbstractBasePlugin):
        class Meta:
            abstract = True
