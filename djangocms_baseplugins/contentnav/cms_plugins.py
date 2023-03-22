from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_formfactory, baseplugin_classfactory
from . import conf
from .models import ContentNav


ContentNavPluginForm = baseplugin_formfactory(ContentNav, conf)
ContentNavPlugin = baseplugin_classfactory(ContentNav, conf, form=ContentNavPluginForm)
plugin_pool.register_plugin(ContentNavPlugin)


# class ContentNavPluginForm(forms.ModelForm):
#     class Meta:
#         model = ContentNav
#         fields = get_fields_from_fieldsets(conf.FIELDSETS)
#         # exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class ContentNavPlugin(BasePluginMixin, CMSPluginBase):
#     model = ContentNav
#     form = ContentNavPluginForm
#     module = module = defaults.ADVANCED_LABEL
#     name = _('ContentNav')
#     render_template = "djangocms_baseplugins/contentnav.html"
#     fieldsets = conf.FIELDSETS
#     allow_children = conf.ALLOW_CHILDREN
#     child_classes = conf.CHILD_CLASSES
