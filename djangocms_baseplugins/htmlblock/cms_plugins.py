# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from . import conf
from .models import HtmlBlock


class HtmlBlockPluginForm(forms.ModelForm):
    class Meta:
        model = HtmlBlock
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'HTMLBLOCKPLUGIN')


class HtmlBlockPlugin(BasePluginMixin, CMSPluginBase):
    model = HtmlBlock
    form = HtmlBlockPluginForm
    module = defaults.ADVANCED_LABEL
    name = _(u'HTML Block')
    render_template = "djangocms_baseplugins/htmlblock.html"
    fieldsets = conf.HTMLBLOCKPLUGIN_FIELDSETS


plugin_pool.register_plugin(HtmlBlockPlugin)
