from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory

from . import conf
from .models import HtmlBlock

HtmlBlockPlugin = baseplugin_classfactory(HtmlBlock, conf)
plugin_pool.register_plugin(HtmlBlockPlugin)


# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from django import forms
# from django.utils.translation import gettext_lazy as _
#
# from djangocms_baseplugins.baseplugin import defaults
# from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
# from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
# from . import conf
# from .models import HtmlBlock
#
#
# class HtmlBlockPluginForm(forms.ModelForm):
#     class Meta:
#         model = HtmlBlock
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# class HtmlBlockPlugin(BasePluginMixin, CMSPluginBase):
#     model = HtmlBlock
#     form = HtmlBlockPluginForm
#     module = defaults.ADVANCED_LABEL
#     name = _(u'HTML Block')
#     render_template = "djangocms_baseplugins/htmlblock.html"
#     fieldsets = conf.FIELDSETS
#
#
# plugin_pool.register_plugin(HtmlBlockPlugin)
