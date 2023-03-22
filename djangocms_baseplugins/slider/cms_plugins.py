from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import Slider


SliderPlugin = baseplugin_classfactory(Slider, conf)
plugin_pool.register_plugin(SliderPlugin)


# # coding: utf-8
# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from django import forms
# from django.utils.translation import gettext_lazy as _
#
# from djangocms_baseplugins.baseplugin import defaults
# from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
# from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets,\
#     get_baseplugin_widgets
# from . import conf
# from .models import Slider
#
#
# class SliderPluginForm(forms.ModelForm):
#     class Meta:
#         model = Slider
#         fields = get_fields_from_fieldsets(conf.FIELDSETS)
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class SliderPlugin(BasePluginMixin, CMSPluginBase):
#     model = Slider
#     form = SliderPluginForm
#     module = defaults.CONTAINER_LABEL
#     name = _(u'Slider')
#     render_template = "djangocms_baseplugins/slider.html"
#     fieldsets = conf.FIELDSETS
#     allow_children = True
#     child_classes = conf.CHILD_CLASSES
