# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import Video
from . import conf


class VideoPluginForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'VIDEOPLUGIN')


class VideoPlugin(BasePluginMixin, CMSPluginBase):
    model = Video
    form = VideoPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTENT_LABEL
    name = _(u'Video')
    render_template = "djangocms_baseplugins/video.html"
    fieldsets = conf.VIDEOPLUGIN_FIELDSETS


plugin_pool.register_plugin(VideoPlugin)
