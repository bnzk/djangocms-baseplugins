# coding: utf-8
from django.conf import settings
from django import forms
from django.core.exceptions import ImproperlyConfigured
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _

from . import defaults

try:
    import bleach
except ImportError:
    bleach = None


def build_baseplugin_fieldset(**kwargs):
    fieldsets = []
    if len(kwargs.get('design', [])):
        fieldsets.append((_('Design & Layout'), {
            'classes': ['fieldset', 'fieldset-design'],
            'fields': kwargs.get('design'),
        }))
    if len(kwargs.get('content', [])):
        fieldsets.append((_('Content'), {
            'classes': ['fieldset', 'fieldset-content'],
            'fields': kwargs.get('content'),
        }))
    if len(kwargs.get('advanced', [])):
        fieldsets.append((_('Advanced Settings'), {
            'classes': ('fieldset', 'fieldset-advanced'),
            'fields': kwargs.get('advanced'),
        }))
    return fieldsets



def get_fields_from_fieldsets(fieldsets):
    fields = []
    for fieldset in fieldsets:
        for field in fieldset[1].get('fields', []):
            fields.append(field)
    return fields


def build_baseplugin_widgets(conf, prefix):
    widgets = {
        'layout': forms.Select(
            choices=getattr(conf, '{}_LAYOUT_CHOICES'.format(prefix), []),
        ),
        'background': forms.Select(
            choices=getattr(conf, '{}_BACKGROUND_CHOICES'.format(prefix), []),
        ),
        'color': forms.Select(
            choices=getattr(conf, '{}_COLOR_CHOICES'.format(prefix), []),
        ),
    }
    return widgets


def check_in_migration_modules(app_name):
    modules = getattr(settings, 'MIGRATION_MODULES', [])
    if not app_name in modules:
        raise ImproperlyConfigured(
            'You need "{}" in settings.MIGRATION_MODULES, or you cannot translat plugins!'
            .format(app_name)
        )


def truncate_richtext_content(richtext):
    return Truncator(strip_tags(richtext).replace('&shy;', '')).words(3, truncate="...")


def sanitize_richtext(text):
    if bleach and defaults.DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG:
        text = bleach.clean(text, **defaults.DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG)
    return text