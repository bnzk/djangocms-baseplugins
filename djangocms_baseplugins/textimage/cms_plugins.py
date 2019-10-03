# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from . import conf
from .models import TextImage


class TextImagePluginForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TextImagePluginForm, self).__init__(*args, **kwargs)
        if not conf.TEXTIMAGEPLUGIN_IMAGE_REQUIRED:
            self.fields['image'].required = False

    class Meta:
        model = TextImage
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'TEXTIMAGEPLUGIN')


class TextImagePlugin(BasePluginMixin, CMSPluginBase):
    model = TextImage
    form = TextImagePluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTENT_LABEL
    name = _(u'Text & Image')
    render_template = "djangocms_baseplugins/textimage.html"
    fieldsets = conf.TEXTIMAGEPLUGIN_FIELDSETS


plugin_pool.register_plugin(TextImagePlugin)
