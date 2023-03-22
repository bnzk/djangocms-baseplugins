# coding: utf-8
from admin_sort.admin.inlines import DragAndDropSortableInlineMixin
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from filer_addons.filer_gui.admin.upload_inline import UploadInlineMixin

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import InlineGallery
from .models import InlineGalleryImage


# class InlineGalleryImageInline(admin.StackedInline):
class InlineGalleryImageInline(
    UploadInlineMixin,
    DragAndDropSortableInlineMixin,
    admin.TabularInline
):
    model = InlineGalleryImage
    file_field = 'image'
    fieldsets = (
        (None, {
            'fields': conf.IMAGE_CONTENT_FIELDS,
        }),
    )
    position_field = 'order'
    extra = 0


InlineGalleryPluginBase = baseplugin_classfactory(InlineGallery, conf)


class InlineGalleryPlugin(InlineGalleryPluginBase):
    render_template = "djangocms_baseplugins/inline_gallery.html"
    inlines = [InlineGalleryImageInline, ]


plugin_pool.register_plugin(InlineGalleryPlugin)


# class InlineGalleryPluginForm(forms.ModelForm):
#     class Meta:
#         model = InlineGallery
#         fields = get_fields_from_fieldsets(conf.INLINEGALLERYPLUGIN_FIELDSETS)
#         # exclude = []
#         widgets = build_baseplugin_widgets(conf, 'INLINEGALLERYPLUGIN')
#
#
# @plugin_pool.register_plugin
# class InlineGalleryPlugin(BasePluginMixin, CMSPluginBase):
#     model = InlineGallery
#     form = InlineGalleryPluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Gallery')
#     render_template = "djangocms_baseplugins/inline_gallery.html"
#     fieldsets = conf.INLINEGALLERYPLUGIN_FIELDSETS
#     inlines = [InlineGalleryImageInline, ]
