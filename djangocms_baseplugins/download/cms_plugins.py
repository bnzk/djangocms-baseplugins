# coding: utf-8

from django import forms
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from modeltranslation.forms import TranslationModelForm

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import Download
from . import conf


# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import DownloadSection
from . import conf


class DownloadSectionPluginForm(forms.ModelForm):
    class Meta:
        model = DownloadSection
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'GALLERY')


@plugin_pool.register_plugin
class DownloadSectionPlugin(BasePluginMixin, CMSPluginBase):
    model = DownloadSection
    form = DownloadSectionPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL
    name = _(u'Downloads')
    render_template = "djangocms_baseplugins/download_section.html"
    fieldsets = conf.DOWNLOADSECTIONPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.DOWNLOADSECTIONPLUGIN_CHILD_CLASSES


class DownloadPluginForm(forms.ModelForm):
    class Meta:
        model = Download
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'DOWNLOADPLUGIN')


@plugin_pool.register_plugin
class DownloadPlugin(BasePluginMixin, CMSPluginBase):
    model = Download
    form = DownloadPluginForm
    # Translators: forget c, this is for alphabetical ordering in cms
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTENT_LABEL
    name = _(u'Download')
    render_template = "djangocms_baseplugins/download.html"
    fieldsets = conf.DOWNLOADPLUGIN_FIELDSETS
