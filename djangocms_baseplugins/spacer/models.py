# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('spacer')


@python_2_unicode_compatible
class SpacerBase(AbstractBasePlugin):
    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Spacer"))
        return self.add_hidden_flag(text)


class Spacer(SpacerBase):
    pass
