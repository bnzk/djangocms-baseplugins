
from django import template


register = template.Library()


@register.filter
def baseplugin_pluginid(plugin_object):
    return 'data-plugin-id="%s"' % plugin_object.pk
