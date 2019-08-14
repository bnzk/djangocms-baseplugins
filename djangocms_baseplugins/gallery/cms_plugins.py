# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import Gallery
from . import conf


class GalleryPluginForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'GALLERY')


class GalleryPlugin(BasePluginMixin, CMSPluginBase):
    model = Gallery
    form = GalleryPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL
    name = _(u'Gallery')
    render_template = "djangocms_baseplugins/gallery.html"
    fieldsets = conf.GALLERYPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.GALLERYPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(GalleryPlugin)