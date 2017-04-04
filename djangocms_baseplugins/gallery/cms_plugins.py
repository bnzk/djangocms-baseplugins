# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Gallery
from . import conf


class GalleryPlugin(BasePluginMixin, CMSPluginBase):
    model = Gallery
    module = _("Containers")
    name = _(u'Gallery')
    render_template = "djangocms_baseplugins/gallery.html"
    fieldsets = conf.GALLERYPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.GALLERYPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(GalleryPlugin)