# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DJANGOCMS_BASEPLUGINS_USE_FILER_ADDONS = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_USE_FILER_ADDONS', True
)


DJANGOCMS_BASEPLUGINS_TRANSLATE = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_TRANSLATE', False
)


DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_TRANSLATED_FIELDS',
    ['title', 'anchor',],
)


DJANGOCMS_BASEPLUGINS_ADVANCED_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_ADVANCED_LABEL',
    _('z Advanced'),
)


DJANGOCMS_BASEPLUGINS_CONTENT_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_CONTENT_LABEL',
    _('Content'),
)


DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL',
    _('Containers'),
)


DJANGOCMS_BASEPLUGINS_MODE = getattr(settings, 'DJANGOCMS_BASEPLUGINS_MODE', 'default')


if DJANGOCMS_BASEPLUGINS_MODE == 'minimal':
    advanced_fields = []
elif DJANGOCMS_BASEPLUGINS_MODE == 'full':
    advanced_fields = [
        ['published', 'in_menu', ],
        ['published_from_date', 'published_until_date', ],
        'anchor',
    ]
else:
    advanced_fields = ['published', ]


BASEPLUGIN_ADVANCED_FIELDS = getattr(settings, 'BASEPLUGIN_ADVANCED_FIELDS', advanced_fields)


WIDTH_CHOICES = getattr(
    settings, 'BASEPLUGIN_WIDTH_CHOICES',
    (
        ('', _('Automatic')),
        ('w-100', _('100%')),
        ('w-66', _('66%')),
        ('w-50', _('50%')),
        ('w-33', _('33%')),
        ('w-25', _('25%')),
    )
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


# set to None for no cleaning on save/render
# this will be passed as kwargs to the bleach.clean() method
DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_BLEACH_CONFIG', {
        'strip': True,
        'tags': DEFAULT_TAGS,
        'attributes': {
            '*': ['class', ],
            'a': allow_attrs_for_a,
        }
    }
)
