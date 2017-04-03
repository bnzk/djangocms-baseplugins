# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

IMAGEPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'IMAGEPLUGIN_CONTENT_FIELDS', (
        'image', 'caption',
    )
)

IMAGEPLUGIN_FIELDSETS = getattr(
    settings,
    'IMAGEPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': [],  # doesnt need this.
        'content': IMAGEPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)
