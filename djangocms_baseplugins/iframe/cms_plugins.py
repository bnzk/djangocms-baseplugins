from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory

from . import conf
from .models import Iframe

IframePlugin = baseplugin_classfactory(
    Iframe,
    conf,
)
plugin_pool.register_plugin(IframePlugin)


# class IframePluginForm(forms.ModelForm):
#     class Meta:
#         model = Iframe
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class IframePlugin(BasePluginMixin, CMSPluginBase):
#     model = Iframe
#     form = IframePluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Iframe')
#     render_template = "djangocms_baseplugins/iframe.html"
#     fieldsets = conf.FIELDSETS
