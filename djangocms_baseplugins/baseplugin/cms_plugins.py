from __future__ import unicode_literals

from django import forms
from cms.models import CMSPlugin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

from djangocms_baseplugins.baseplugin.utils import is_edit_mode
from . import defaults


if defaults.TRANSLATE:
    from djangocms_misc.basic.admin import LanguageTabsMixin


    class BasePluginMixinBase(LanguageTabsMixin, TranslationAdmin):
        pass


    class BaseInlineMixinBase(TranslationInlineModelAdmin):
        pass


else:


    class BasePluginMixinBase(object):
        pass


    class BaseInlineMixinBase(object):
        pass


class ParentPluginFormMixin(object):
    """
    mostly used when fine grained control of child plugins forms is needed
    - hide/show fields, based on parent plugin type/field values
    - different choices, based on parent plugin type/field values
    """
    def __init__(self, *args, **kwargs):
        super_result = super().__init__(*args, **kwargs)
        parent = None
        if kwargs.get('initial', None):
            if kwargs['initial'].get('plugin_parent', None):
                parent = CMSPlugin.objects.get(pk=kwargs['initial']['plugin_parent'])
        elif self.instance.parent:
            parent = self.instance.parent
        self.parent_plugin = parent
        if parent:
            self.parent_plugin_instance, plugin = parent.get_plugin_instance()
        return super_result


class BasePluginMixin(BasePluginMixinBase):

    def get_render_template(self, context, instance, placeholder):
        request = context.get('request', None)
        if not instance.is_visible() and not is_edit_mode(request.toolbar):
            return 'djangocms_baseplugins/unpublished.html'
        return self.render_template

    def render(self, context, instance, placeholder):
        context['plugin'] = self
        context['object'] = instance
        context['placeholder'] = placeholder
        return context


class BasePluginInlineMixin(BaseInlineMixinBase):
    pass
