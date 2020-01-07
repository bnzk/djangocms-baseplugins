# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset

TEASERSECTIONPLUGIN_TRANSLATED_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_TRANSLATED_FIELDS', []
)

TEASERSECTIONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_CONTENT_FIELDS', []
)

TEASERSECTIONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_DESIGN_FIELDS', []
)

TEASERSECTIONPLUGIN_FIELDSETS = getattr(
    settings,
    'TEASERSECTIONPLUGIN_FIELDSETS',
    get_baseplugin_fieldset(**{
        'design': TEASERSECTIONPLUGIN_DESIGN_FIELDS,
        'content': TEASERSECTIONPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)

TEASERSECTIONPLUGIN_CHILD_CLASSES = getattr(
    settings, 'TEASERSECTIONPLUGIN_CHILD_CLASSES', (
        'TextImagePlugin',
        # or your own, custom teaser plugin
    )
)
