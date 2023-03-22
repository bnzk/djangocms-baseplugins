from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_formfactory, baseplugin_classfactory
from . import conf
from .models import Text


TextPluginForm = baseplugin_formfactory(Text, conf)
TextPlugin = baseplugin_classfactory(Text, conf, form=TextPluginForm)
plugin_pool.register_plugin(TextPlugin)


# class TextPluginForm(forms.ModelForm):
#     class Meta:
#         model = Text
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class TextPlugin(BasePluginMixin, CMSPluginBase):
#     model = Text
#     form = TextPluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Text')
#     render_template = "djangocms_baseplugins/text.html"
#     fieldsets = conf.FIELDSETS
#     require_parent = conf.REQUIRE_PARENT
