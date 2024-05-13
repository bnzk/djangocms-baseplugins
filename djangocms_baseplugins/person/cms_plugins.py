from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import (
    baseplugin_classfactory,
    baseplugin_formfactory,
)

from . import conf_person, conf_section
from .models import Person, PersonSection

PersonSectionPlugin = baseplugin_classfactory(PersonSection, conf_section)
PersonSectionPlugin.render_template = "djangocms_baseplugins/person_section.html"
plugin_pool.register_plugin(PersonSectionPlugin)


PersonPluginForm = baseplugin_formfactory(Person, conf_person)
PersonPlugin = baseplugin_classfactory(Person, conf_person, form=PersonPluginForm)
plugin_pool.register_plugin(PersonPlugin)


# class PersonSectionPluginForm(forms.ModelForm):
#     class Meta:
#         model = PersonSection
#         exclude = []
#         widgets = build_baseplugin_widgets(conf, 'PERSONSECTIONPLUGIN')
#
#
# class PersonSectionPlugin(BasePluginMixin, CMSPluginBase):
#     model = PersonSection
#     form = PersonSectionPluginForm
#     module = defaults.CONTAINER_LABEL
#     name = _(u'People Section')
#     render_template = "djangocms_baseplugins/person_section.html"
#     allow_children = True
#     child_classes = ('PersonPlugin',)
#     fieldsets = conf.PERSONSECTIONPLUGIN_FIELDSETS
#
#
# plugin_pool.register_plugin(PersonSectionPlugin)
#
#
# class PersonPluginForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         exclude = []
#         widgets = build_baseplugin_widgets(conf, 'PERSONPLUGIN')
#
#
# class PersonPlugin(BasePluginMixin, CMSPluginBase):
#     model = Person
#     form = PersonPluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Person / Contact')
#     render_template = "djangocms_baseplugins/person.html"
#     require_parent = True
#     fieldsets = conf.PERSONPLUGIN_FIELDSETS
#
#
# plugin_pool.register_plugin(PersonPlugin)
