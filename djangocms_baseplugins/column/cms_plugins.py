# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import Column
from . import conf


class ColumnPluginForm(forms.ModelForm):
    width = forms.ChoiceField(choices=conf.COLUMNPLUGIN_WIDTH_CHOICES )

    class Meta:
        model = Column
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'COLUMN')


class ColumnPlugin(BasePluginMixin, CMSPluginBase):
    model = Column
    form = ColumnPluginForm
    name = _(u'Column')
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL
    render_template = "djangocms_baseplugins/column.html"
    fieldsets = conf.COLUMNPLUGIN_FIELDSETS
    require_parent = True
    allow_children = True
    child_classes = conf.COLUMNPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(ColumnPlugin)
