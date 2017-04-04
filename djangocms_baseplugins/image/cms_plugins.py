# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Image
from . import conf


class ImagePlugin(BasePluginMixin, CMSPluginBase):
    model = Image
    module = _("A) Content")
    name = _(u'Image')
    render_template = "djangocms_baseplugins/image.html"
    fieldsets = conf.IMAGEPLUGIN_FIELDSETS

plugin_pool.register_plugin(ImagePlugin)
