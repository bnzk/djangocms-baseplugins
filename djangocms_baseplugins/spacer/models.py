from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("spacer")


class SpacerBase(AbstractBasePlugin):
    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Spacer"))
        return self.add_hidden_flag(text)


class Spacer(SpacerBase):
    pass
