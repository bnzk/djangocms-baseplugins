# coding: utf-8
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.image.models import ImageBase


@python_2_unicode_compatible
class InlineGalleryBase(AbstractBasePlugin):
    height = models.CharField(_('Height'), max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Gallery"))
        return self.add_hidden_flag(text)


class InlineGallery(InlineGalleryBase):
    pass


class InlineGalleryImage(ImageBase):
    gallery = models.ForeignKey(
        'gallery_inline.InlineGallery',
    )
