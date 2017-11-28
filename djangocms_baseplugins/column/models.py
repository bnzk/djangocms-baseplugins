# coding: utf-8
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class ColumnBase(AbstractBasePlugin):
    width = models.CharField(_('width'), max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Column"))
        return self.add_hidden_flag(text)


class Column(ColumnBase):
    pass
