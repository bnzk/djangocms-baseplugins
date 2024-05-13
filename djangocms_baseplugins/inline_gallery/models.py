from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

from .base import InlineGalleryBase, InlineGalleryImageBase

check_migration_modules_needed("inline_gallery")


class InlineGallery(InlineGalleryBase):
    pass


class InlineGalleryImage(InlineGalleryImageBase):
    def __str__(self):
        return self.to_string()
