# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import TextImage
from . import conf


class TextImagePluginForm(forms.ModelForm):
    class Meta:
        model = TextImage
        exclude = []
        widgets = {
            'layout': forms.Select(choices=conf.TEXTIMAGEPLUGIN_LAYOUT_CHOICES)
        }


class TextImagePlugin(BasePluginMixin, CMSPluginBase):
    model = TextImage
    form = TextImagePluginForm
    module = _("Content")
    name = _(u'Text & Image')
    render_template = "djangocms_baseplugins/textimage.html"
    fieldsets = conf.TEXTIMAGEPLUGIN_FIELDSETS

plugin_pool.register_plugin(TextImagePlugin)