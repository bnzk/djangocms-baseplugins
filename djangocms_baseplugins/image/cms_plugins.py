# coding: utf-8

from django import forms
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from modeltranslation.forms import TranslationModelForm

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import Image
from . import conf


class ImagePluginForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'IMAGEPLUGIN')


class ImagePlugin(BasePluginMixin, CMSPluginBase):
    model = Image
    form = ImagePluginForm
    # Translators: forget c, this is for alphabetical ordering in cms
    module = _("Content")
    name = _(u'Image')
    render_template = "djangocms_baseplugins/image.html"
    fieldsets = conf.IMAGEPLUGIN_FIELDSETS


plugin_pool.register_plugin(ImagePlugin)
