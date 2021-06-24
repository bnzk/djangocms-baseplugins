from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import Spacer


SpacerPlugin = baseplugin_classfactory(Spacer, conf)
plugin_pool.register_plugin(SpacerPlugin)



# # coding: utf-8
# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from django import forms
# from django.utils.translation import ugettext_lazy as _
#
# from djangocms_baseplugins.baseplugin import defaults
# from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
# from djangocms_baseplugins.baseplugin.utils import get_fields_from_fieldsets, get_baseplugin_widgets
# from . import conf
# from .models import Spacer
#
#
# class SpacerPluginForm(forms.ModelForm):
#     class Meta:
#         model = Spacer
#         fields = get_fields_from_fieldsets(conf.FIELDSETS)
#         # exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# class SpacerPlugin(BasePluginMixin, CMSPluginBase):
#     model = Spacer
#     form = SpacerPluginForm
#     module = defaults.SPECIAL_LABEL
#     name = _(u'Spacer')
#     render_template = "djangocms_baseplugins/spacer.html"
#     fieldsets = conf.FIELDSETS
#
#
# plugin_pool.register_plugin(SpacerPlugin)
