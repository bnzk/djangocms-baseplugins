from __future__ import unicode_literals


class BasePluginMixin():

    def get_render_template(self, context, instance, placeholder):
        request = context.get('request', None)
        if not instance.published and not request.toolbar.edit_mode:
            self.render_template = 'djangocms_baseplugins/unpublished.html'

    def render(self, context, instance, placeholder):
        context['plugin'] = self
        context['object'] = instance
        context['placeholder'] = placeholder
        return context
