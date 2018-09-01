# coding: utf-8
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from .models import ContentNav
from . import conf


class ContentNavPluginForm(forms.ModelForm):

    class Meta:
        model = ContentNav
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'CONTENTNAV')


class ContentNavPlugin(BasePluginMixin, CMSPluginBase):
    model = ContentNav
    form = ContentNavPluginForm
    module = _("Containers")
    name = _('ContentNav')
    render_template = "djangocms_baseplugins/contentnav.html"
    fieldsets = conf.CONTENTNAVPLUGIN_FIELDSETS


plugin_pool.register_plugin(ContentNavPlugin)
