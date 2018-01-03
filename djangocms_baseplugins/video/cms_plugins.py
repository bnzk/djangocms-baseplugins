# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Video
from . import conf


class VideoPluginForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = []
        widgets = {
            'layout': forms.Select(choices=conf.VIDEOPLUGIN_LAYOUT_CHOICES)
        }


class VideoPlugin(BasePluginMixin, CMSPluginBase):
    model = Video
    form = VideoPluginForm
    module = _("Content")
    name = _(u'Video')
    render_template = "djangocms_baseplugins/text.html"
    fieldsets = conf.VIDEOPLUGIN_FIELDSETS


plugin_pool.register_plugin(VideoPlugin)
