# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from filer_addons.filer_gui.admin.upload_inline import UploadInlineMixin

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import InlineGallery, InlineGalleryImage
from . import conf


# class InlineGalleryImageInline(admin.StackedInline):
class InlineGalleryImageInline(UploadInlineMixin, admin.StackedInline):
    model = InlineGalleryImage
    file_field = 'image'
    extra = 0


class InlineGalleryPluginForm(forms.ModelForm):

    class Meta:
        model = InlineGallery
        fields = get_fields_from_fieldsets(conf.INLINEGALLERYPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'INLINEGALLERY')


class InlineGalleryPlugin(BasePluginMixin, CMSPluginBase):
    model = InlineGallery
    form = InlineGalleryPluginForm
    module = _("Containers")
    name = _(u'Gallery')
    render_template = "djangocms_baseplugins/inline_gallery.html"
    fieldsets = conf.INLINEGALLERYPLUGIN_FIELDSETS
    inlines = [InlineGalleryImageInline, ]
    allow_children = True
    child_classes = conf.INLINEGALLERYPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(InlineGalleryPlugin)