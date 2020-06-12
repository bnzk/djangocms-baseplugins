# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets, get_baseplugin_widgets
from . import conf
from .models import Contact


class ContactPluginForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = get_fields_from_fieldsets(conf.FIELDSETS)
        widgets = get_baseplugin_widgets(conf)


@plugin_pool.register_plugin
class ContactPlugin(BasePluginMixin, CMSPluginBase):
    model = Contact
    form = ContactPluginForm
    module = defaults.CONTENT_LABEL
    name = _(u'Contact')
    render_template = "djangocms_baseplugins/contact.html"
    fieldsets = conf.FIELDSETS
    readonly_fields = ('lat', 'lng', 'geo_error',)
    allow_children = True
    child_classes = conf.CHILD_CLASSES
