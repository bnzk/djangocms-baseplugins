from .base import ImagePluginBase
from ..baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed('image')


class Image(ImagePluginBase):
    pass
