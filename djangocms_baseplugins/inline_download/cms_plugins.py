# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from filer_addons.filer_gui.admin.upload_inline import UploadInlineMixin
from admin_sort.admin.inlines import DragAndDropSortableInlineMixin

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin, BasePluginInlineMixin
from djangocms_baseplugins.baseplugin.utils import (
    build_baseplugin_widgets,
    get_fields_from_fieldsets,
)
from . import conf
from .models import InlineDownload, InlineDownloadEntry


# class InlineDownloadImageInline(admin.StackedInline):
class InlineDownloadEntryInline(
    UploadInlineMixin,
    DragAndDropSortableInlineMixin,
    BasePluginInlineMixin,
    admin.StackedInline,
):
    model = InlineDownloadEntry
    file_field = 'file'
    fieldsets = (
        (None, {
            'fields': conf.INLINEDOWNLOADPLUGIN_ENTRY_CONTENT_FIELDS,
        }),
    )
    extra = 0
    position_field = 'order'


class InlineDownloadPluginForm(forms.ModelForm):
    class Meta:
        model = InlineDownload
        fields = get_fields_from_fieldsets(conf.INLINEDOWNLOADPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'INLINEDOWNLOADPLUGIN')


@plugin_pool.register_plugin
class InlineDownloadPlugin(BasePluginMixin, CMSPluginBase):
    model = InlineDownload
    form = InlineDownloadPluginForm
    module = defaults.CONTENT_LABEL
    name = _(u'Downloads')
    render_template = "djangocms_baseplugins/inline_download.html"
    fieldsets = conf.INLINEDOWNLOADPLUGIN_FIELDSETS
    inlines = [InlineDownloadEntryInline, ]
