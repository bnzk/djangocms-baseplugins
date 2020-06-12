# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
from . import conf
from .models import Video


class VideoPluginForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = []
        widgets = get_baseplugin_widgets(conf)


@plugin_pool.register_plugin
class VideoPlugin(BasePluginMixin, CMSPluginBase):
    model = Video
    form = VideoPluginForm
    module = defaults.CONTENT_LABEL
    name = _(u'Video')
    render_template = "djangocms_baseplugins/video.html"
    fieldsets = conf.FIELDSETS
