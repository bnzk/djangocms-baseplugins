# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset

HTMLBLOCKPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'HTMLBLOCKPLUGIN_CONTENT_FIELDS', (
        'htmlblock',
    )
)

HTMLBLOCKPLUGIN_FIELDSETS = getattr(
    settings,
    'HTMLBLOCKPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': [],  # htmlblock doesnt need this.
        'content': HTMLBLOCKPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })

)
