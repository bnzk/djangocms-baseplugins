# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import (
    get_fields_from_fieldsets, build_baseplugin_widgets
)
from djangocms_baseplugins.baseplugin import defaults

from .models import AutoColumns
from . import conf


class AutoColumnsPluginForm(forms.ModelForm):
    class Meta:
        model = AutoColumns
        fields = get_fields_from_fieldsets(conf.FIELDSETS)
        widgets = build_baseplugin_widgets(conf, 'AUTOCOLUMNSPLUGIN')


@plugin_pool.register_plugin
class AutoColumnsPlugin(BasePluginMixin, CMSPluginBase):
    model = AutoColumns
    name = _(u'Auto Multiple Columns')
    form = AutoColumnsPluginForm
    module = defaults.CONTAINER_LABEL
    render_template = "djangocms_baseplugins/autocolumns.html"
    fieldsets = conf.FIELDSETS
    allow_children = True
    child_classes = conf.CHILD_CLASSES
