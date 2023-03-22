from cms.models.fields import PageField
from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed('contentnav')


class ContentNavBase(AbstractBasePlugin):
    menu_depth = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Depth")
    )
    cms_page = PageField(
        null=True,
        default=None,
        blank=True,
        help_text=_("Show submenu of this page")
    )
    sitemap = models.BooleanField(
        default=False,
        help_text=_("Show complete sitemap")
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("of this very page"))
        if self.cms_page:
            text = str(_("of %s")) % str(self.cms_page)
        elif self.sitemap:
            text = str(_("Complete sitemap"))
        return self.add_hidden_flag(text)


class ContentNav(ContentNavBase):
    pass
