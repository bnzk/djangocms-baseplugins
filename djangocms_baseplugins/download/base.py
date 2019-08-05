# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin import defaults


if defaults.DJANGOCMS_BASEPLUGINS_USE_FILER_ADDONS:
    from filer_addons.filer_gui.fields import FilerFileField
else:
    from filer.fields.file import FilerFileField


class DownloadBase(models.Model):
    file = FilerFileField(
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_download",
        verbose_name=_("Download"),
    )
    link_text = models.CharField(
        max_length=255,
        default='',
        blank=True,
    )

    class Meta:
        abstract = True

    def to_string(self):
        text = None
        if self.link_text:
            text = '%s, %s' % (self.link_text, self.file)
        if not text:
            text = '%s' % (self.file)
        return text


class DownloadPluginBase(AbstractBasePlugin, DownloadBase):

    class Meta:
        abstract = True
