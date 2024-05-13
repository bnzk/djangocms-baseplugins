from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.download.base import DownloadBase


class InlineDownloadBase(AbstractBasePlugin):
    height = models.CharField(
        _("Height"),
        max_length=32,
        default="",
        blank=True,
    )

    class Meta:
        abstract = True

    def to_string(self):
        text = str(_("Downloads"))
        return self.add_hidden_flag(text)

    def copy_relations(self, old_instance):
        super(InlineDownloadBase, self).copy_relations(old_instance)
        # self.images.add(*old_instance.images.all())
        for entry in old_instance.downloads.all():
            entry.id = None
            entry.save()
            self.downloads.add(entry)


class InlineDownloadEntryBase(DownloadBase):
    inline_download = models.ForeignKey(
        "inline_download.InlineDownload",
        related_name="downloads",
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.to_string()

    class Meta:
        ordering = ("order",)
        abstract = True
