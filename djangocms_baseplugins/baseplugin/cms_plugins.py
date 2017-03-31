# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


class BasePluginMixin():

    def render(self, context, instance, placeholder):
        if not instance.published:
            self.render_template = 'baseplugin/unpublished.html'
        context['plugin'] = self
        context['object'] = instance
        context['placeholder'] = placeholder
        return context
