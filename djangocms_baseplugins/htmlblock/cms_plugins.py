# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import HtmlBlock
from . import conf


class HtmlBlockPlugin(BasePluginMixin, CMSPluginBase):
    model = HtmlBlock
    module = _("C) Advanced")
    name = _(u'HTML Block')
    render_template = "djangocms_baseplugins/htmlblock.html"
    fieldsets = conf.HTMLBLOCKPLUGIN_FIELDSETS

plugin_pool.register_plugin(HtmlBlockPlugin)
