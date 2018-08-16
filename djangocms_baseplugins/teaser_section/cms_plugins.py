# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets, get_fields_from_fieldsets
from .models import TeaserSection
from . import conf


class TeaserSectionPluginForm(forms.ModelForm):
    class Meta:
        model = TeaserSection
        fields = get_fields_from_fieldsets(conf.TEASERSECTIONPLUGIN_FIELDSETS)
        # exclude = []
        widgets = build_baseplugin_widgets(conf, 'TEASERSECTION')


class TeaserSectionPlugin(BasePluginMixin, CMSPluginBase):
    model = TeaserSection
    form = TeaserSectionPluginForm
    module = _("Containers")
    name = _('Teaser Section')
    render_template = "djangocms_baseplugins/teaser_section.html"
    fieldsets = conf.TEASERSECTIONPLUGIN_FIELDSETS
    allow_children = True
    child_classes = conf.TEASERSECTIONPLUGIN_CHILD_CLASSES


plugin_pool.register_plugin(TeaserSectionPlugin)
