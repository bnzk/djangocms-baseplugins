from ..baseplugin.utils import check_migration_modules_needed
from .base import ImagePluginBase

check_migration_modules_needed("image")


class Image(ImagePluginBase):
    pass
