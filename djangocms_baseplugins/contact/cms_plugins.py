# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import Contact
from . import conf


class ContactPluginForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = get_fields_from_fieldsets(conf.CONTACTPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'CONTACTPLUGIN')


class ContactPlugin(BasePluginMixin, CMSPluginBase):
    model = Contact
    form = ContactPluginForm
    module = _("Content")
    name = _(u'Contact')
    render_template = "djangocms_baseplugins/contact.html"
    fieldsets = conf.CONTACTPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.CONTACTPLUGIN_CHILD_CLASSES


plugin_pool.register_plugin(ContactPlugin)
