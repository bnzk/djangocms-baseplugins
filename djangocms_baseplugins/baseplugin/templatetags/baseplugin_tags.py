from django import template

from ..utils import sanitize_richtext

register = template.Library()


@register.filter
def baseplugin_pluginid(plugin_object):
    return 'data-plugin-id="%s"' % plugin_object.pk


@register.filter
def baseplugin_sanitize_richtext(text):
    return sanitize_richtext(text)
