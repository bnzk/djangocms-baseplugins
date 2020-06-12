# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class SectionBase(AbstractBasePlugin):
    height = models.CharField(_('Height'), max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def to_string(self):
        if self.title:
            return self.title
        return str(_("Section"))


class Section(SectionBase):
    pass
