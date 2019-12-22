# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import (
    get_fields_from_fieldsets,
    build_baseplugin_widgets,
)
from . import conf
from .models import Spacer


class SpacerPluginForm(forms.ModelForm):
    class Meta:
        model = Spacer
        fields = get_fields_from_fieldsets(conf.SPACERPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'SPACERPLUGIN')


class SpacerPlugin(BasePluginMixin, CMSPluginBase):
    model = Spacer
    form = SpacerPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_SPECIAL_LABEL
    name = _(u'Spacer')
    render_template = "djangocms_baseplugins/spacer.html"
    fieldsets = conf.SPACERPLUGIN_FIELDSETS


plugin_pool.register_plugin(SpacerPlugin)
