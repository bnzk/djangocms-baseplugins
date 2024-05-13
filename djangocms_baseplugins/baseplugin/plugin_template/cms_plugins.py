# coding: utf-8
from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory

from . import conf
from .models import PluginTemplate

PluginTemplatePlugin = baseplugin_classfactory(PluginTemplate, conf)
plugin_pool.register_plugin(PluginTemplatePlugin)


# class PluginTemplatePluginForm(forms.ModelForm):
#     class Meta:
#         model = PluginTemplate
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class PluginTemplatePlugin(BasePluginMixin, CMSPluginBase):
#     model = PluginTemplate
#     form = PluginTemplatePluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'PluginTemplate')
#     render_template = "djangocms_baseplugins/plugintemplate.html"
#     fieldsets = conf.FIELDSETS
#     allow_children = conf.ALLOW_CHILDREN
#     child_classes = conf.CHILD_CLASSES
