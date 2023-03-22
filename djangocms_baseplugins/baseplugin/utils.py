from collections.abc import Iterable

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults


try:
    import bleach
except ImportError:
    bleach = None

try:
    basestring
except NameError:
    basestring = str

try:
    from lxml.html import clean as lxml_clean, fragment_fromstring, tostring
except ImportError:
    lxml_clean = None


DEFAULT_MINIMAL_SETTINGS = (
    'NAME',
    'MODULE',
    'ALLOW_CHILDREN',
    'TO_STRING_ADD_ATTRS',
    'CHILD_CLASSES',
    'REQUIRE_PARENT',
    'TRANSLATED_FIELDS',
    'CONTENT_FIELDS',
    'DESIGN_FIELDS',
    'ADVANCED_FIELDS',
    'LAYOUT_CHOICES',
    'SIZE_CHOICES',
    'BACKGROUND_CHOICES',
    'COLOR_CHOICES',
    'CUSTOM_CHOICES',
)


def check_settings(prefix, conf, settings):
    # Default settings that all plugins have
    for setting in DEFAULT_MINIMAL_SETTINGS:
        _check_one_setting(prefix, conf, settings, setting)
    # Custom settings for a plugin
    for setting in dir(conf):
        # bad way to test if it is a setting!
        if setting == setting.upper() and setting not in DEFAULT_MINIMAL_SETTINGS:
            _check_one_setting(prefix, conf, settings, setting)
    # Labels and help texts
    for field_setting in ['CONTENT_FIELDS', 'DESIGN_FIELDS', 'ADVANCED_FIELDS']:
        for field in flatten(getattr(conf, field_setting)):
            _check_one_setting(prefix, conf, settings, 'LABEL_{}'.format(field.upper()))
            _check_one_setting(prefix, conf, settings, 'HELP_TEXT_{}'.format(field.upper()))


def _check_one_setting(prefix, conf, settings, setting):
    # old style
    global_setting_name = '{}_{}'.format(prefix, setting)
    value = getattr(settings, global_setting_name, None)
    # new style
    dict_settings = getattr(settings, prefix, None)
    if dict_settings:
        value = dict_settings.get(setting, None)
    if value:
        setattr(conf, setting, value)
    elif getattr(conf, setting, None) is None:
        # fallback, when a plugin is not up to date with settings
        setattr(conf, setting, getattr(defaults, setting, None))


def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item


# DEPRECATED
def build_baseplugin_fieldset(**kwargs):
    return get_baseplugin_fieldset(**kwargs)


def get_baseplugin_fieldset(**kwargs):
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
            if isinstance(field, basestring):
                fields.append(field)
            else:
                for sub_field in field:
                    fields.append(sub_field)
    return fields


# DEPRECATED
def build_baseplugin_widgets(conf, prefix):
    widgets = {
        'layout': forms.Select(
            choices=getattr(conf, '{}_LAYOUT_CHOICES'.format(prefix), []),
        ),
        'size': forms.Select(
            choices=getattr(conf, '{}_SIZE_CHOICES'.format(prefix), []),
        ),
        'background': forms.Select(
            choices=getattr(conf, '{}_BACKGROUND_CHOICES'.format(prefix), []),
        ),
        'color': forms.Select(
            choices=getattr(conf, '{}_COLOR_CHOICES'.format(prefix), []),
        ),
        'custom': forms.Select(
            choices=getattr(conf, '{}_CUSTOM_CHOICES'.format(prefix), []),
        ),
    }
    return widgets


def get_baseplugin_widgets(conf):
    widgets = {
        'layout': forms.Select(
            choices=getattr(conf, 'LAYOUT_CHOICES', []),
        ),
        'size': forms.Select(
            choices=getattr(conf, 'SIZE_CHOICES', []),
        ),
        'background': forms.Select(
            choices=getattr(conf, 'BACKGROUND_CHOICES', []),
        ),
        'color': forms.Select(
            choices=getattr(conf, 'COLOR_CHOICES', []),
        ),
        'custom': forms.Select(
            choices=getattr(conf, 'CUSTOM_CHOICES', []),
        ),
    }
    return widgets


def check_in_migration_modules(app_name):
    # TODO: legacy warning
    check_migration_modules_needed(app_name)


def check_migration_modules_needed(app_name):
    modules = getattr(settings, 'MIGRATION_MODULES', [])
    needs_check = False
    if getattr(settings, 'DJANGOCMS_BASEPLUGINS_TRANSLATE', None):
        needs_check = True
    if getattr(settings, 'DJANGOCMS_BASEPLUGINS_BASEMODEL', None):
        needs_check = True
    if needs_check:
        if app_name not in modules:
            raise ImproperlyConfigured(
                'You need "{}" in settings.MIGRATION_MODULES, '
                'or you cannot translate plugins, or have a custom abstract baseplugin!'
                .format(app_name)
            )


def truncate_richtext_content(richtext):
    return Truncator(strip_tags(richtext).replace('&shy;', '')).words(3, truncate="...")


def sanitize_richtext(text):
    if defaults.LXML_CLEANER_CONFIG:
        if lxml_clean:
            lxml_cleaner = lxml_clean.Cleaner(**defaults.LXML_CLEANER_CONFIG)
            fragment = fragment_fromstring("<div>" + text + "</div>")
            fragment = lxml_cleaner.clean_html(fragment)
            text = tostring(fragment, encoding='unicode')
            if text.startswith('<div>'):
                # still dont like lxml!
                text = text[len('<div>'):-len('</div>')]
        elif settings.DEBUG:
            print("lxml is not installed, but should be, for sanitizing richtext content!")
    if defaults.BLEACH_CONFIG:
        if bleach:
            text = bleach.clean(text, **defaults.BLEACH_CONFIG)
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
