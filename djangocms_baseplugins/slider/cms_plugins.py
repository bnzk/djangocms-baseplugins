# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import Slider
from . import conf


class SliderPluginForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = get_fields_from_fieldsets(conf.SLIDERPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'SLIDERPLUGIN')


class SliderPlugin(BasePluginMixin, CMSPluginBase):
    model = Slider
    form = SliderPluginForm
    module = _("Containers")
    name = _(u'Slider')
    render_template = "djangocms_baseplugins/slider.html"
    fieldsets = conf.SLIDERPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.SLIDERPLUGIN_CHILD_CLASSES


plugin_pool.register_plugin(SliderPlugin)
