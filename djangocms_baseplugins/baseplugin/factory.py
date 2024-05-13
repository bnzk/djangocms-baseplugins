from cms.plugin_base import CMSPluginBase
from django import forms

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.forms import BasePluginFormMixin
from djangocms_baseplugins.baseplugin.utils import (
    get_baseplugin_widgets,
    get_fields_from_fieldsets,
)


def baseplugin_classfactory(model_class, conf, form=None, more_mixin_classes=[]):
    class_name = model_class.__name__
    super_classes = more_mixin_classes + [BasePluginMixin, CMSPluginBase]
    super_classes = tuple(super_classes)
    if not form:
        form = baseplugin_formfactory(model_class, conf)
    module, sep, tail = model_class.__module__.rpartition(".models")
    attrs = {
        "__module__": module + ".cms_plugins",
        "model": model_class,
        "form": form,
        "module": getattr(conf, "MODULE", defaults.CONTENT_LABEL),
        "name": getattr(conf, "NAME", class_name),
        "render_template": "djangocms_baseplugins/{}.html".format(class_name.lower()),
        "fieldsets": getattr(conf, "FIELDSETS", []),
        "allow_children": getattr(conf, "ALLOW_CHILDREN", False),
        "child_classes": getattr(conf, "CHILD_CLASSES", None),
        "require_parent": getattr(conf, "REQUIRE_PARENT", False),
    }
    cls = type("{}Plugin".format(class_name), super_classes, attrs)
    return cls


def baseplugin_formfactory(model_class, conf, additional_widgets={}):
    # build meta inner class
    fields = get_fields_from_fieldsets(conf.FIELDSETS)
    widgets = get_baseplugin_widgets(conf)
    widgets.update(additional_widgets)
    meta_attrs = {
        "model": model_class,
        "fields": fields,
        "widgets": widgets,
        "labels": {},
        "help_texts": {},
    }
    # customize via settings
    for field in fields:
        # label
        settings_attr = "LABEL_{}".format(field.upper())
        value = getattr(conf, settings_attr, None)
        if value:
            meta_attrs["labels"][field] = value
        # help_text
        settings_attr = "HELP_TEXT_{}".format(field.upper())
        value = getattr(conf, settings_attr, None)
        if value:
            meta_attrs["help_texts"][field] = value
        # widget
        settings_attr = "WIDGET_{}".format(field.upper())
        value = getattr(conf, settings_attr, None)
        if value:
            widgets[field] = value
    meta = type(
        "Meta",
        (
            BasePluginFormMixin,
            forms.ModelForm,
        ),
        meta_attrs,
    )
    # build form class itself
    form_attrs = {
        "Meta": meta,
    }
    return type(
        "{}PluginForm",
        (
            BasePluginFormMixin,
            forms.ModelForm,
        ),
        form_attrs,
    )
