from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

from .base import InlineDownloadBase, InlineDownloadEntryBase

check_migration_modules_needed("inline_download")


class InlineDownload(InlineDownloadBase):
    pass


class InlineDownloadEntry(InlineDownloadEntryBase):
    pass
