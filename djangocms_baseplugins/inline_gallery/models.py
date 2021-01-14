# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from .base import InlineGalleryBase, InlineGalleryImageBase
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('inline_gallery')


class InlineGallery(InlineGalleryBase):
    pass


@python_2_unicode_compatible
class InlineGalleryImage(InlineGalleryImageBase):

    def __str__(self):
        return self.to_string()
