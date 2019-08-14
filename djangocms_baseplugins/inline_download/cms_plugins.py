# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from filer_addons.filer_gui.admin.upload_inline import UploadInlineMixin

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import InlineDownload, InlineDownloadEntry
from . import conf


# class InlineDownloadImageInline(admin.StackedInline):
class InlineDownloadEntryInline(UploadInlineMixin, admin.StackedInline):
    model = InlineDownloadEntry
    file_field = 'file'
    fieldsets = (
        (None, {
            'fields': conf.INLINEDOWNLOADPLUGIN_ENTRY_CONTENT_FIELDS,
        }),
    )
    extra = 0


class InlineDownloadPluginForm(forms.ModelForm):
    class Meta:
        model = InlineDownload
        fields = get_fields_from_fieldsets(conf.INLINEDOWNLOADPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'INLINEDOWNLOAD')


class InlineDownloadPlugin(BasePluginMixin, CMSPluginBase):
    model = InlineDownload
    form = InlineDownloadPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL
    name = _(u'Downloads')
    render_template = "djangocms_baseplugins/inline_download.html"
    fieldsets = conf.INLINEDOWNLOADPLUGIN_FIELDSETS
    inlines = [InlineDownloadEntryInline, ]


plugin_pool.register_plugin(InlineDownloadPlugin)
