from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf_section
from . import conf_entry
from .models import DownloadSection
from .models import Download


DownloadSectionPlugin = baseplugin_classfactory(DownloadSection, conf_section)
plugin_pool.register_plugin(DownloadSectionPlugin)

DownloadPlugin = baseplugin_classfactory(Download, conf_entry)
plugin_pool.register_plugin(DownloadPlugin)


# class DownloadSectionPluginForm(forms.ModelForm):
#     class Meta:
#         model = DownloadSection
#         exclude = []
#         widgets = get_baseplugin_widgets(conf_section)
#
#
# @plugin_pool.register_plugin
# class DownloadSectionPlugin(BasePluginMixin, CMSPluginBase):
#     model = DownloadSection
#     form = DownloadSectionPluginForm
#     module = defaults.CONTAINER_LABEL
#     name = _(u'Downloads')
#     render_template = "djangocms_baseplugins/download_section.html"
#     fieldsets = conf.FIELDSETS
#     allow_children = True
#     child_classes = conf.CHILD_CLASSES
#
#
# class DownloadPluginForm(forms.ModelForm):
#     class Meta:
#         model = Download
#         exclude = []
#         widgets = build_baseplugin_widgets(conf_entry, 'DOWNLOADPLUGIN')
#
#
# @plugin_pool.register_plugin
# class DownloadPlugin(BasePluginMixin, CMSPluginBase):
#     model = Download
#     form = DownloadPluginForm
#     # Translators: forget c, this is for alphabetical ordering in cms
#     module = defaults.CONTENT_LABEL
#     name = _(u'Download')
#     render_template = "djangocms_baseplugins/download.html"
#     fieldsets = conf_entry.FIELDSETS
