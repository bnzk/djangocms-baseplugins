# coding: utf-8
import requests
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import HtmlBlock
from . import conf


class HtmlBlockPlugin(BasePluginMixin, CMSPluginBase):
    model = HtmlBlock
    name = _(u'htmlblock')
    render_template = "htmlblock/htmlblock.html"
    fieldsets = conf.HTMLBLOCKPLUGIN_FIELDSETS

plugin_pool.register_plugin(HtmlBlockPlugin)
