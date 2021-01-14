# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


check_migration_modules_needed('autocolumns')


class AutoColumns(AbstractBasePlugin):

    def to_string(self):
        if self.title:
            return self.title
        return str(_("Auto Multiple Columns"))
