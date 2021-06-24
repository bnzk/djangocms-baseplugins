from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory, baseplugin_formfactory
from . import conf
from .models import TextImage


def textimage_init(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if not conf.IMAGE_REQUIRED:
        self.fields['image'].required = False


TextImagePluginForm = baseplugin_formfactory(TextImage, conf)
TextImagePluginForm.__init__ = textimage_init
TextImagePlugin = baseplugin_classfactory(TextImage, conf)
plugin_pool.register_plugin(TextImagePlugin)


# # coding: utf-8
# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from django import forms
# from django.utils.translation import ugettext_lazy as _
#
# from djangocms_baseplugins.baseplugin import defaults
# from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
# from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
# from . import conf
# from .models import TextImage
#
#
# class TextImagePluginForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super(TextImagePluginForm, self).__init__(*args, **kwargs)
#         if not conf.IMAGE_REQUIRED:
#             self.fields['image'].required = False
#
#     class Meta:
#         model = TextImage
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class TextImagePlugin(BasePluginMixin, CMSPluginBase):
#     model = TextImage
#     form = TextImagePluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Text & Image')
#     render_template = "djangocms_baseplugins/textimage.html"
#     fieldsets = conf.FIELDSETS
#     require_parent = conf.REQUIRE_PARENT
