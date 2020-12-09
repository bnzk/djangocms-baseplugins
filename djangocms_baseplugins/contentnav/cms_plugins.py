# coding: utf-8
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets, get_baseplugin_widgets
from . import conf
from .models import ContentNav


class ContentNavPluginForm(forms.ModelForm):
    class Meta:
        model = ContentNav
        fields = get_fields_from_fieldsets(conf.FIELDSETS)
        # exclude = []
        widgets = get_baseplugin_widgets(conf)


@plugin_pool.register_plugin
class ContentNavPlugin(BasePluginMixin, CMSPluginBase):
    model = ContentNav
    form = ContentNavPluginForm
    module = module = defaults.ADVANCED_LABEL
    name = _('ContentNav')
    render_template = "djangocms_baseplugins/contentnav.html"
    fieldsets = conf.FIELDSETS
    allow_children = conf.ALLOW_CHILDREN
    child_classes = conf.CHILD_CLASSES
