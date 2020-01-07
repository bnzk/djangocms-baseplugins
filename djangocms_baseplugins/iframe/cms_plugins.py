# coding: utf-8

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
from . import conf
from .models import Iframe


class IframePluginForm(forms.ModelForm):
    class Meta:
        model = Iframe
        exclude = []
        widgets = get_baseplugin_widgets(conf)


@plugin_pool.register_plugin
class IframePlugin(BasePluginMixin, CMSPluginBase):
    model = Iframe
    form = IframePluginForm
    module = defaults.CONTENT_LABEL
    name = _(u'Iframe')
    render_template = "djangocms_baseplugins/iframe.html"
    fieldsets = conf.FIELDSETS
