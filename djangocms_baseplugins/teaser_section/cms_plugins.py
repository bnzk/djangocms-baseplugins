# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import TeaserSection
from . import conf


class TeaserSectionPlugin(BasePluginMixin, CMSPluginBase):
    model = TeaserSection
    module = _("containers")
    name = _('teaser section')
    render_template = "teaser_section/teaser_section.html"
    fieldsets = conf.TEASERSECTIONPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.TEASERSECTIONPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(TeaserSectionPlugin)