# coding: utf-8
from django.conf import settings
from django import forms
from django.core.exceptions import ImproperlyConfigured
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


def truncate_richtext_content(richtext):
    return Truncator(strip_tags(richtext).replace('&shy;', '')).words(3, truncate="...")


def check_in_migration_modules(app_name):
    modules = getattr(settings, 'MIGRATION_MODULES', [])
    if not app_name in modules:
        raise ImproperlyConfigured(
            'You need "{}" in settings.MIGRATION_MODULES, or you cannot translat plugins!'
            .format(app_name)
        )
