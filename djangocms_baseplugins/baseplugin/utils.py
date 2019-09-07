# coding: utf-8
from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _

from . import defaults

try:
    import bleach
except ImportError:
    bleach = None

try:
    from lxml.html import clean as lxml_clean, fragment_fromstring, tostring
except ImportError:
    lxml_clean = None


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
            choices=getattr(conf, '{}PLUGIN_LAYOUT_CHOICES'.format(prefix), []),
        ),
        'background': forms.Select(
            choices=getattr(conf, '{}PLUGIN_BACKGROUND_CHOICES'.format(prefix), []),
        ),
        'color': forms.Select(
            choices=getattr(conf, '{}PLUGIN_COLOR_CHOICES'.format(prefix), []),
        ),
    }
    return widgets


def check_in_migration_modules(app_name):
    modules = getattr(settings, 'MIGRATION_MODULES', [])
    if app_name not in modules:
        raise ImproperlyConfigured(
            'You need "{}" in settings.MIGRATION_MODULES, or you cannot translat plugins!'
            .format(app_name)
        )


def truncate_richtext_content(richtext):
    return Truncator(strip_tags(richtext).replace('&shy;', '')).words(3, truncate="...")


def sanitize_richtext(text):
    if defaults.DJANGOCMS_BASEPLUGINS_LXML_CLEANER_CONFIG:
        if lxml_clean:
            lxml_cleaner = lxml_clean.Cleaner(**defaults.DJANGOCMS_BASEPLUGINS_LXML_CLEANER_CONFIG)
            fragment = fragment_fromstring("<div>" + text + "</div>")
            fragment = lxml_cleaner.clean_html(fragment)
            text = tostring(fragment, encoding='unicode')
            if text.startswith('<div>'):
                # still dont like lxml!
                text = text[len('<div>'):-len('</div>')]
        elif settings.DEBUG:
            print("lxml is not installed, but should be, for sanitizing richtext content!")
    if defaults.DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG:
        if bleach:
            text = bleach.clean(text, **defaults.DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG)
        elif settings.DEBUG:
            print("bleach is not installed, but should be, for sanitizing richtext content!")
    return text


def is_edit_mode(toolbar):
    if (
        getattr(toolbar, 'edit_mode', None) or  # cms pre 3.6
        getattr(toolbar, 'edit_mode_active', None) or  # cms 3.6+
        getattr(toolbar, 'build_mode', None) or
        getattr(toolbar, 'build_mode_active', None)
    ):
        return True
    return False
