# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Spacer
from . import conf

class SpacerPlugin(BasePluginMixin, CMSPluginBase):
    model = Spacer
    name = _(u'Spacer')
    render_template = "djangocms_baseplugins/spacer.html"
    fieldsets = conf.SPACERPLUGIN_FIELDSETS
    require_parent = True
    allow_children = True
    child_classes = conf.SPACERPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(SpacerPlugin)
