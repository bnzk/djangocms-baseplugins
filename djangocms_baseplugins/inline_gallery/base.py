from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.image.base import ImageBase


class InlineGalleryBase(AbstractBasePlugin):
    description = models.TextField(
        blank=True,
        default='',
    )
    height = models.CharField(
        _('Height'),
        max_length=32,
        default='',
        blank=True,
    )

    class Meta:
        abstract = True

    def to_string(self):
        text = str(_("Gallery"))
        return self.add_hidden_flag(text)

    def copy_relations(self, old_instance):
        super(InlineGalleryBase, self).copy_relations(old_instance)
        # self.images.add(*old_instance.images.all())
        for entry in old_instance.images.all():
            entry.id = None
            entry.save()
            self.images.add(entry)


class InlineGalleryImageBase(ImageBase):
    gallery = models.ForeignKey(
        'inline_gallery.InlineGallery',
        related_name='images',
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ('order',)
        abstract = True
