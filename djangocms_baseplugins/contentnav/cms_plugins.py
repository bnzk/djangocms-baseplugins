# coding: utf-8
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import ContentNav
from . import conf


class ContentNavPluginForm(forms.ModelForm):

    class Meta:
        model = ContentNav
        fields = get_fields_from_fieldsets(conf.CONTENTNAVPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'CONTENTNAVPLUGIN')


class ContentNavPlugin(BasePluginMixin, CMSPluginBase):
    model = ContentNav
    form = ContentNavPluginForm
    module = _("Containers")
    name = _('ContentNav')
    render_template = "djangocms_baseplugins/contentnav.html"
    fieldsets = conf.CONTENTNAVPLUGIN_FIELDSETS


plugin_pool.register_plugin(ContentNavPlugin)
