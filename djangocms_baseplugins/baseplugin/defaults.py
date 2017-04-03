# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DJANGOCMS_BASEPLUGINS_MODE = getattr(settings, 'DJANGOCMS_BASEPLUGINS_MODE', 'default')

if DJANGOCMS_BASEPLUGINS_MODE == 'minimal':
    content_fields = []
    design_fields = []
    advanced_fields = []
elif DJANGOCMS_BASEPLUGINS_MODE == 'full':
    content_fields = ['title', ]
    design_fields = ['layout', 'background', 'color', ]
    advanced_fields = ['published', 'in_menu', 'anchor', ]
else:
    content_fields = ['title', ]
    design_fields = ['layout', ]
    advanced_fields = ['published', ]

BASEPLUGIN_CONTENT_FIELDS = getattr(settings, 'BASEPLUGIN_DESIGN_FIELDS', content_fields)
BASEPLUGIN_DESIGN_FIELDS = getattr(settings, 'BASEPLUGIN_DESIGN_FIELDS', design_fields)
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