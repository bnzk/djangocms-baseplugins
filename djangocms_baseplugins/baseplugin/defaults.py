import sys

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# Filter Addons, Translation
USE_FILER_ADDONS = True
TRANSLATE = False
TRANSLATED_FIELDS = ['title', 'anchor', ]

# Module labels
CONTENT_LABEL = _('A - Content')
CONTAINER_LABEL = _('B - Containers')
SPECIAL_LABEL = _('C - Special')
ADVANCED_LABEL = _('Z - Advanced')

# basic defaults for plugins
NAME = 'override, please'
MODULE = CONTENT_LABEL
TO_STRING_ADD_ATTRS = False  # show attrs in to_string?

# Fields
CONTENT_FIELDS = []
DESIGN_FIELDS = []

# Advanced fields, with Mode
MODE = 'default'
if MODE == 'minimal':
    advanced_fields = []
elif MODE == 'full':
    advanced_fields = [
        ['published', 'in_menu', ],
        ['published_from_date', 'published_until_date', ],
        'anchor',
    ]
else:
    advanced_fields = ['published', ]

ADVANCED_FIELDS = advanced_fields

ATTR_FIELDS = (
    'layout',
    'size',
    'background',
    'color',
    'custom',
    'width',  # column only
)

# Some choices defaults
WIDTH_CHOICES = (
    ('', _('Automatic')),
    ('w-100', _('100%')),
    ('w-66', _('66%')),
    ('w-50', _('50%')),
    ('w-33', _('33%')),
    ('w-25', _('25%')),
)
LAYOUT_CHOICES = (
    ('', _('Automatic')),
    ('one', _('Layout One')),
    ('two', _('Layout Two')),
)
SIZE_CHOICES = (
    ('', _('Automatic')),
    ('big', _('Big')),
    ('small', _('Small')),
)
BACKGROUND_CHOICES = (
    ('', _('Automatic')),
    ('white', _('White')),
    ('grey', _('Grey')),
)
COLOR_CHOICES = (
    ('', _('Automatic')),
    ('green', _('Green')),
    ('yello', _('Yellow')),
)
CUSTOM_CHOICES = (
    ('', _('---')),
    ('none', _('Have not')),
    ('give', _('Have')),
)


def allow_attrs_for_a(tag, name, value):
    """
    allow data-* attributes
    """
    if name.startswith('data-'):
        return True
    if name in ['href', 'target', 'title', 'rel', 'class', ]:
        return True


DEFAULT_TAGS = [
    'h1',
    'h2',
    'h3',
    'h4',
    'p',
    'span',
    'br',
    'a',
    'hr',
    'strong',
    'b',
    'em',
    'i',
    'ul',
    'ol',
    'li',
]

TABLE_TAGS = [
    'table',
    'tr',
    'th',
    'td',
]

BLEACH_CONFIG_DEFAULT = {
    'strip': True,
    'tags': DEFAULT_TAGS,
    'attributes': {
        '*': ['class', ],
        'a': allow_attrs_for_a,
    }
}

# set to None for no cleaning on save/render
# this will be passed as kwargs to the bleach.clean() method
BLEACH_CONFIG = None

# set to None for no cleaning on save/render
# this will be passed as kwargs to the lxml.html.clean.Cleaner constructor
# explanations: https://lxml.de/api/lxml.html.clean.Cleaner-class.html
LXML_CLEANER_CONFIG =  {
    'scripts': True,
    'javascript': True,
    'comments': True,
    'style': True,
    'inline_style': True,
    'links': True,
    'meta': True,
    'page_structure': True,
    'processing_instructions': True,
    'embedded': True,
    'frames': True,
    'forms': True,
    'annoying_tags': False,
    # dont have these in basic richtext content!
    'remove_tags': ['section', 'div', 'nav', 'footer', ],
    'allow_tags': None,
    'kill_tags': None,
    'remove_unknown_tags': True,
    'safe_attrs_only': False,
    'safe_attrs': None,
    'add_nofollow': False,
    'host_whitelist': [],
    # 'whitelist_tags':
}


def check_settings(prefix, conf, settings):
    for setting in dir(conf):
        # bad way to test if it is a setting!
        if setting == setting.upper():
            _check_one_setting(prefix, conf, settings, setting)
    # Labels and help texts
    for field in ('title', 'layout', 'size', 'background', 'color', 'custom', 'anchor', 'published', 'in_menu', ):
        _check_one_setting(prefix, conf, settings, 'LABEL_{}'.format(field))
        _check_one_setting(prefix, conf, settings, 'HELP_TEXT_{}'.format(field))


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


# use this
check_settings('DJANGOCMS_BASEPLUGINS', sys.modules[__name__], settings)
# works as well
check_settings('BASEPLUGINS', sys.modules[__name__], settings)
