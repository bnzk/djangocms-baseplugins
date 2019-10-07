# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


class AutoColumns(AbstractBasePlugin):

    def to_string(self):
        text = _('Auto Multiple Columns')
        return text
