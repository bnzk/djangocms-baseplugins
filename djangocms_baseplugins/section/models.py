from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("section")


class SectionBase(AbstractBasePlugin):
    height = models.CharField(_("Height"), max_length=32, default="", blank=True)

    class Meta:
        abstract = True

    def to_string(self):
        if self.title:
            return self.title
        return str(_("Section"))


class Section(SectionBase):
    pass
