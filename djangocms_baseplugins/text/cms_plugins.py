# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Text
from . import conf


class TextPluginForm(forms.ModelForm):
    class Meta:
        model = Text
        exclude = []
        widgets = {
            'layout': forms.Select(choices=conf.TEXTPLUGIN_LAYOUT_CHOICES)
        }


class TextPlugin(BasePluginMixin, CMSPluginBase):
    model = Text
    form = TextPluginForm
    module = _("Content")
    name = _(u'Text')
    render_template = "djangocms_baseplugins/text.html"
    fieldsets = conf.TEXTPLUGIN_FIELDSETS

plugin_pool.register_plugin(TextPlugin)
