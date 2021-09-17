from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

from . import conf

check_migration_modules_needed('autocolumns')


class AutoColumns(AbstractBasePlugin):

    def to_string(self):
        text = ''  # str(_("Auto Columns"))
        if self.title:
            text = self.title
        return self.attrs_to_string(text, conf)
