from admin_sort.admin.inlines import DragAndDropSortableInlineMixin
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from filer_addons.filer_gui.admin.upload_inline import UploadInlineMixin

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import InlineDownload, InlineDownloadEntry
from ..baseplugin.cms_plugins import BasePluginInlineMixin


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
            'fields': conf.ENTRY_CONTENT_FIELDS,
        }),
    )
    extra = 0
    position_field = 'order'


InlineDownloadPluginBase = baseplugin_classfactory(InlineDownload, conf)


class InlineDownloadPlugin(InlineDownloadPluginBase):
    render_template = "djangocms_baseplugins/inline_download.html"
    inlines = [InlineDownloadEntryInline, ]


plugin_pool.register_plugin(InlineDownloadPlugin)


# class InlineDownloadPluginForm(forms.ModelForm):
#     class Meta:
#         model = InlineDownload
#         fields = get_fields_from_fieldsets(conf.INLINEDOWNLOADPLUGIN_FIELDSETS)
#         # exclude = []
#         widgets = build_baseplugin_widgets(conf, 'INLINEDOWNLOADPLUGIN')
#
#
# @plugin_pool.register_plugin
# class InlineDownloadPlugin(BasePluginMixin, CMSPluginBase):
#     model = InlineDownload
#     form = InlineDownloadPluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Downloads')
#     render_template = "djangocms_baseplugins/inline_download.html"
#     fieldsets = conf.INLINEDOWNLOADPLUGIN_FIELDSETS
#     inlines = [InlineDownloadEntryInline, ]
