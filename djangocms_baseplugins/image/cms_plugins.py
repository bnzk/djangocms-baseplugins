# coding: utf-8

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from . import conf
from .models import Image


class ImagePluginForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'IMAGEPLUGIN')


@plugin_pool.register_plugin
class ImagePlugin(BasePluginMixin, CMSPluginBase):
    model = Image
    form = ImagePluginForm
    # Translators: forget c, this is for alphabetical ordering in cms
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTENT_LABEL
    name = _(u'Image')
    render_template = "djangocms_baseplugins/image.html"
    fieldsets = conf.IMAGEPLUGIN_FIELDSETS
