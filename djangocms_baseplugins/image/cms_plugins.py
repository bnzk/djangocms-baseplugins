# coding: utf-8

# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from django import forms
# from django.utils.translation import ugettext_lazy as _
#
# from djangocms_baseplugins.baseplugin import defaults
# from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
# from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import Image

ImagePlugin = baseplugin_classfactory(Image, conf)
plugin_pool.register_plugin(ImagePlugin)


# class ImagePluginForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class ImagePlugin(BasePluginMixin, CMSPluginBase):
#     model = Image
#     form = ImagePluginForm
#     # Translators: forget c, this is for alphabetical ordering in cms
#     module = defaults.CONTENT_LABEL
#     name = _(u'Image')
#     render_template = "djangocms_baseplugins/image.html"
#     fieldsets = conf.FIELDSETS
