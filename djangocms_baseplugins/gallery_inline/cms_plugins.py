# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import InlineGallery, InlineGalleryImage
from . import conf


class InlineGalleryImageInline(admin.TabularInline):
    model = InlineGalleryImage
    extra = 0


class InlineGalleryPluginForm(forms.ModelForm):
    class Meta:
        model = InlineGallery
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'INLINEGALLERY')


class InlineGalleryPlugin(BasePluginMixin, CMSPluginBase):
    model = InlineGallery
    form = InlineGalleryPluginForm
    module = _("Containers")
    name = _(u'Gallery')
    render_template = "djangocms_baseplugins/gallery.html"
    fieldsets = conf.INLINEGALLERYPLUGIN_FIELDSETS
    inlines = [InlineGalleryImageInline, ]
    allow_children = True
    child_classes = conf.INLINEGALLERYPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(InlineGalleryPlugin)