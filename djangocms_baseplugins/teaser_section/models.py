from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('teaser_section')


class TeaserSectionBase(AbstractBasePlugin):
    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Teaser Section"))
        return self.add_hidden_flag(text)


class TeaserSection(TeaserSectionBase):
    pass
