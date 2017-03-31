# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


BASEPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'BASEPLUGIN_DESIGN_FIELDS', (
        ('layout', 'background', 'color', ),
    )
)

BASEPLUGIN_ADVANCED_FIELDS = getattr(
    settings, 'BASEPLUGIN_ADVANCED_FIELDS', (
        ('published', 'in_menu', ),
        'anchor',
    )
)

WIDTH_CHOICES = getattr(
    settings, 'BASEPLUGIN_WIDTH_CHOICES',
    (
        ('', _('automatic')),
        ('w-100', _('100%')),
        ('w-66', _('66%')),
        ('w-50', _('50%')),
        ('w-33', _('33%')),
    )
)