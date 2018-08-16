# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import Section
from . import conf


class SectionPluginForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = get_fields_from_fieldsets(conf.SECTIONPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'SECTIONPLUGIN')


class SectionPlugin(BasePluginMixin, CMSPluginBase):
    model = Section
    form = SectionPluginForm
    module = _("Containers")
    name = _(u'Section')
    render_template = "djangocms_baseplugins/section.html"
    fieldsets = conf.SECTIONPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.SECTIONPLUGIN_CHILD_CLASSES


plugin_pool.register_plugin(SectionPlugin)
