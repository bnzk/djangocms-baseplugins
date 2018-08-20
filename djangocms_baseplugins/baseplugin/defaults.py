# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

DJANGOCMS_BASEPLUGINS_USE_FILER_ADDONS = getattr(
    settings,
    'DJANGOCMS_BASEPLUGINS_USE_FILER_ADDONS', False
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
