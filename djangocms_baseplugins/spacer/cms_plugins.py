# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Spacer
from . import conf


class SpacerPluginForm(forms.ModelForm):
    class Meta:
        model = Spacer
        exclude = []
        widgets = {
            'layout': forms.Select(choices=conf.SPACERPLUGIN_LAYOUT_CHOICES)
        }


class SpacerPlugin(BasePluginMixin, CMSPluginBase):
    model = Spacer
    form = SpacerPluginForm
    module = _("Content")
    name = _(u'Spacer')
    render_template = "djangocms_baseplugins/spacer.html"
    fieldsets = conf.SPACERPLUGIN_FIELDSETS


plugin_pool.register_plugin(SpacerPlugin)
