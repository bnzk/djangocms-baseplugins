# coding: utf-8
from __future__ import unicode_literals

from .base import InlineDownloadBase, InlineDownloadEntryBase
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('inline_download')


class InlineDownload(InlineDownloadBase):
    pass


class InlineDownloadEntry(InlineDownloadEntryBase):
    pass
