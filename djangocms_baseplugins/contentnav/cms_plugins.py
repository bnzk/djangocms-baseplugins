# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import ContentNav
from . import conf


class ContentNavPluginForm(forms.ModelForm):
    width = forms.ChoiceField(choices=conf.CONTENTNAVPLUGIN_WIDTH_CHOICES )

    class Meta:
        model = ContentNav
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'CONTENTNAV')


class ContentNavPlugin(BasePluginMixin, CMSPluginBase):
    model = ContentNav
    form = ContentNavPluginForm
    name = _(u'ContentNav')
    render_template = "djangocms_baseplugins/contentnav.html"
    fieldsets = conf.CONTENTNAVPLUGIN_FIELDSETS
    require_parent = True
    allow_children = True
    child_classes = conf.CONTENTNAVPLUGIN_CHILD_CLASSES

plugin_pool.register_plugin(ContentNavPlugin)