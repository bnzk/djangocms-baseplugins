# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Person, PersonSection

from . import conf


class PersonSectionPlugin(BasePluginMixin, CMSPluginBase):
    model = PersonSection
    module = _("containers")
    name = _(u'person section')
    render_template = "person/person_section.html"
    allow_children = True
    child_classes = ('PersonPlugin', )
    fieldsets = conf.PERSONSECTIONPLUGIN_FIELDSETS

plugin_pool.register_plugin(PersonSectionPlugin)


class PersonPlugin(BasePluginMixin, CMSPluginBase):
    model = Person
    module = _("content")
    name = _(u'person')
    render_template = "person/person.html"
    require_parent = True
    fieldsets = conf.PERSONPLUGIN_FIELDSETS

plugin_pool.register_plugin(PersonPlugin)
