# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin

if defaults.USE_FILER_ADDONS:
    from filer_addons.filer_gui.fields import FilerImageField
else:
    from filer.fields.image import FilerImageField


class ImageBase(models.Model):
    image = FilerImageField(
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_image",
        verbose_name=_("Image"),
    )
    caption = models.CharField(
        max_length=255,
        default='',
        blank=True,
    )
    alt_text = models.CharField(
        max_length=255,
        default='',
        blank=True,
    )

    class Meta:
        abstract = True

    def to_string(self):
        text = None
        if self.caption:
            text = '%s, %s' % (self.caption, self.image)
        if self.alt_text:
            text = '%s, %s' % (self.alt_text, self.image)
        if not text:
            text = '%s' % (self.image)
        return text


class ImagePluginBase(AbstractBasePlugin, ImageBase):
    class Meta:
        abstract = True
