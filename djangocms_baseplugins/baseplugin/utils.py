# coding: utf-8
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _


def build_baseplugin_fieldset(**kwargs):
    fieldset = []
    if len(kwargs.get('design', [])):
        fieldset.append((_('Design & Layout'), {
            'classes': ['fieldset', 'fieldset-design'],
            'fields': kwargs.get('design'),
        }))
    if len(kwargs.get('content', [])):
        fieldset.append((_('Content'), {
            'classes': ['fieldset', 'fieldset-content'],
            'fields': kwargs.get('content'),
        }))
    if len(kwargs.get('advanced', [])):
        fieldset.append((_('Advanced Settings'), {
            'classes': ('fieldset', 'fieldset-advanced'),
            'fields': kwargs.get('advanced'),
        }))
    return fieldset


def truncate_richtext_content(richtext):
    return Truncator(strip_tags(richtext).replace('&shy;', '')).words(3, truncate="...")
