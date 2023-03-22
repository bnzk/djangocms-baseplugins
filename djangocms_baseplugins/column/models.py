from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

from . import conf


check_migration_modules_needed('column')


class ColumnBase(AbstractBasePlugin):
    width = models.CharField(_('width'), max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def to_string(self):
        text = ''
        if self.title:
            text = self.title
        return self.attrs_to_string(text, conf)

    def css_classes(self):
        classes = super(ColumnBase, self).css_classes()
        classes += self._css_modifier_for_field('width')
        return classes


class Column(ColumnBase):
    pass
