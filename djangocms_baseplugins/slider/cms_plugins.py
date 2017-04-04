# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Slider
from . import conf


class SliderPlugin(BasePluginMixin, CMSPluginBase):
    model = Slider
    module = _("B) Containers")
    name = _(u'Slider')
    render_template = "djangocms_baseplugins/slider.html"
    fieldsets = conf.SLIDERPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.SLIDERPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(SliderPlugin)