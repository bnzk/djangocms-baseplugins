# coding: utf-8
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.image.base import ImageBase


@python_2_unicode_compatible
class InlineGalleryBase(AbstractBasePlugin):
    height = models.CharField(
        _('Height'),
        max_length=32,
        default='',
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Gallery"))
        return self.add_hidden_flag(text)

    def copy_relations(self, old_instance):
        super(InlineGalleryBase, self).copy_relations(old_instance)
        # self.images.add(*old_instance.images.all())
        for entry in old_instance.images.all():
            entry.id = None
            entry.save()
            self.images.add(entry);


class InlineGallery(InlineGalleryBase):
    pass


class InlineGalleryImageBase(ImageBase):
    gallery = models.ForeignKey(
        'inline_gallery.InlineGallery',
        related_name='images',
    )
    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ('order', )
        abstract = True


class InlineGalleryImage(InlineGalleryImageBase):
    pass