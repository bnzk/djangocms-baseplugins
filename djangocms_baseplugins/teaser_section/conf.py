# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

TEASERSECTIONPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_CONTENT_FIELDS', (
        'title',
    )
)

TEASERSECTIONPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'TEASERSECTIONPLUGIN_DESIGN_FIELDS', (
        'layout',
    )
)

TEASERSECTIONPLUGIN_FIELDSETS = getattr(
    settings,
    'TEASERSECTIONPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
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
