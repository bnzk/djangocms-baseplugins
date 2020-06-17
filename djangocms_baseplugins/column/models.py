# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


class ColumnBase(AbstractBasePlugin):
    width = models.CharField(_('width'), max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def to_string(self):
        if self.title:
            return self.title
        text = str(_("Column"))
        return text

    def get_css_classes(self):
        classes = super(ColumnBase, self).get_css_classes()
        classes += self._css_modifier_for_field('width')
        return classes


class Column(ColumnBase):
    pass
