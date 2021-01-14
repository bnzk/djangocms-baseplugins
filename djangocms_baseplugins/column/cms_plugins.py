# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets, get_baseplugin_widgets
from . import conf
from .models import Column

# some pre processing
column_widgets = get_baseplugin_widgets(conf)
column_widgets.update({
    'width': forms.Select(
        choices=getattr(conf, 'WIDTH_CHOICES', []),
    ),
})


class ColumnPluginForm(forms.ModelForm):
    # width = forms.ChoiceField(choices=conf.COLUMNPLUGIN_WIDTH_CHOICES)

    class Meta:
        model = Column
        exclude = []
        fields = get_fields_from_fieldsets(conf.FIELDSETS)
        widgets = column_widgets


@plugin_pool.register_plugin
class ColumnPlugin(BasePluginMixin, CMSPluginBase):
    model = Column
    form = ColumnPluginForm
    name = _(u'Column')
    module = defaults.CONTAINER_LABEL
    render_template = "djangocms_baseplugins/column.html"
    fieldsets = conf.FIELDSETS
    require_parent = True
    allow_children = True
    child_classes = conf.CHILD_CLASSES
