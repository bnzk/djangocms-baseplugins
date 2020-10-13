from cms.plugin_base import CMSPluginBase
from django import forms

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets


def baseplugin_classfactory(model_class, conf, form=None, super_classes=[]):
    class_name = model_class.__name__
    super_classes += [BasePluginMixin, CMSPluginBase]
    super_classes = tuple(super_classes)
    if not form:
        form = baseplugin_formfactory(model_class, conf)
    attrs = {
        'model': model_class,
        'form': form,
        'module': getattr(conf, 'MODULE', defaults.CONTENT_LABEL),
        'name': getattr(conf, 'NAME', class_name),
        'render_template': "djangocms_baseplugins/{}.html".format(class_name.lower()),
        'fieldsets': getattr(conf, 'FIELDSETS', []),
        'allow_children': getattr(conf, 'ALLOW_CHILDREN', False),
        'child_classes': getattr(conf, 'CHILD_CLASSES', []),
        'require_parent': getattr(conf, 'REQUIRE_PARENT', False),
    }
    return type('{}Plugin'.format(class_name), super_classes, attrs)


def baseplugin_formfactory(model_class, conf):
    # build meta inner class
    attrs = {
        'model': model_class,
        'exclude': [],
        'widgets': get_baseplugin_widgets(conf),
    }
    meta = type('Meta', tuple(), attrs)
    # build form class itself
    form_attrs = {
        'Meta': meta,
    }
    return type('{}PluginForm', (forms.ModelForm, ), form_attrs)