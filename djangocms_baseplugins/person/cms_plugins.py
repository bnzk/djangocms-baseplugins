# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_widgets
from . import conf
from .models import Person, PersonSection


class PersonSectionPluginForm(forms.ModelForm):
    class Meta:
        model = PersonSection
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'PERSONSECTION')


class PersonSectionPlugin(BasePluginMixin, CMSPluginBase):
    model = PersonSection
    form = PersonSectionPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL
    name = _(u'People Section')
    render_template = "djangocms_baseplugins/person_section.html"
    allow_children = True
    child_classes = ('PersonPlugin',)
    fieldsets = conf.PERSONSECTIONPLUGIN_FIELDSETS


plugin_pool.register_plugin(PersonSectionPlugin)


class PersonPluginForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []
        widgets = build_baseplugin_widgets(conf, 'PERSON')


class PersonPlugin(BasePluginMixin, CMSPluginBase):
    model = Person
    form = PersonPluginForm
    module = defaults.DJANGOCMS_BASEPLUGINS_CONTENT_LABEL
    name = _(u'Person / Contact')
    render_template = "djangocms_baseplugins/person.html"
    require_parent = True
    fieldsets = conf.PERSONPLUGIN_FIELDSETS


plugin_pool.register_plugin(PersonPlugin)
