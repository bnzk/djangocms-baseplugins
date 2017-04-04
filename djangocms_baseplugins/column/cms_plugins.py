# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Column
from . import conf

class ColumnPlugin(BasePluginMixin, CMSPluginBase):
    model = Column
    name = _(u'Column')
    render_template = "djangocms_baseplugins/column.html"
    fieldsets = conf.COLUMNPLUGIN_FIELDSETS
    require_parent = True
    allow_children = True
    child_classes = conf.COLUMNPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(ColumnPlugin)