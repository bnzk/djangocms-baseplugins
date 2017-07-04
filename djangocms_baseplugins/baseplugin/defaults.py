# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DJANGOCMS_BASEPLUGINS_MODE = getattr(settings, 'DJANGOCMS_BASEPLUGINS_MODE', 'default')

if DJANGOCMS_BASEPLUGINS_MODE == 'minimal':
    advanced_fields = []
elif DJANGOCMS_BASEPLUGINS_MODE == 'full':
    advanced_fields = [['published', 'in_menu', ], 'anchor', ]
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
    )
)
