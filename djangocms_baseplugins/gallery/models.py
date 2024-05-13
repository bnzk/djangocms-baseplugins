from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("gallery")


class GalleryBase(AbstractBasePlugin):
    description = models.TextField(
        blank=True,
        default="",
    )
    height = models.CharField(_("Height"), max_length=32, default="", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Gallery"))
        return self.add_hidden_flag(text)


class Gallery(GalleryBase):
    pass
