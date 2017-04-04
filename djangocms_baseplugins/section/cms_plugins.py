# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Section
from . import conf


class SectionPlugin(BasePluginMixin, CMSPluginBase):
    model = Section
    module = _("Containers")
    name = _(u'Section')
    render_template = "djangocms_baseplugins/section.html"
    fieldsets = conf.SECTIONPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.SECTIONPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(SectionPlugin)