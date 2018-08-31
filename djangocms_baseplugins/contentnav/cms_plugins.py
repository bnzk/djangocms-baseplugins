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

    def render(self, context, instance, placeholder):
        # TODO: prepare if a different than the current page is selected, to show the menu of...
        context = super(ContentNavPlugin, self).render(context, instance, placeholder)
        page = getattr(context["request"], 'current_page', None)
        context.update({
            'contentnav_page': page
        })
        return context


plugin_pool.register_plugin(ContentNavPlugin)
