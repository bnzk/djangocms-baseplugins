from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory
from . import conf
from .models import Contact


ContactPluginBase = baseplugin_classfactory(Contact, conf)


class ContactPlugin(ContactPluginBase):
    readonly_fields = ('lat', 'lng', 'geo_error',)


plugin_pool.register_plugin(ContactPlugin)


# class ContactPluginForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = get_fields_from_fieldsets(conf.FIELDSETS)
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class ContactPlugin(BasePluginMixin, CMSPluginBase):
#     model = Contact
#     form = ContactPluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Contact')
#     render_template = "djangocms_baseplugins/contact.html"
#     fieldsets = conf.FIELDSETS
#     readonly_fields = ('lat', 'lng', 'geo_error',)
#     allow_children = True
#     child_classes = conf.CHILD_CLASSES
