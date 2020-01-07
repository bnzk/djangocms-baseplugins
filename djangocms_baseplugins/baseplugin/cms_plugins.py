from __future__ import unicode_literals

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
