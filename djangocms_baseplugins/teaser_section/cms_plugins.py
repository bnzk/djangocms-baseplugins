from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import TeaserSection


TeaserSectionPlugin = baseplugin_classfactory(TeaserSection, conf)
plugin_pool.register_plugin(TeaserSectionPlugin)


# # coding: utf-8
# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from django import forms
# from django.utils.translation import ugettext_lazy as _
#
# from djangocms_baseplugins.baseplugin import defaults
# from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
# from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets, \
#     get_baseplugin_widgets
# from . import conf
# from .models import TeaserSection
#
#
# class TeaserSectionPluginForm(forms.ModelForm):
#     class Meta:
#         model = TeaserSection
#         fields = get_fields_from_fieldsets(conf.FIELDSETS)
#         # exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class TeaserSectionPlugin(BasePluginMixin, CMSPluginBase):
#     model = TeaserSection
#     form = TeaserSectionPluginForm
#     module = defaults.CONTAINER_LABEL
#     name = _('Teaser Section')
#     render_template = "djangocms_baseplugins/teaser_section.html"
#     fieldsets = conf.FIELDSETS
#     allow_children = True
#     child_classes = conf.CHILD_CLASSES
