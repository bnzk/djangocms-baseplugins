# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from .base import DownloadPluginBase
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


class DownloadSectionBase(AbstractBasePlugin):

    class Meta:
        abstract = True

    def to_string(self):
        if not self.title:
            text = str(_("Downloads"))
        else:
            text = self.title
        return text


class DownloadSection(DownloadSectionBase):
    pass


class Download(DownloadPluginBase):
    pass
