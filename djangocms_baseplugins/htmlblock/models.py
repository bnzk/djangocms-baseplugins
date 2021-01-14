from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('htmlblock')


class HtmlBlockBase(AbstractBasePlugin):
    htmlblock = models.TextField(verbose_name=_("HTML Block"), help_text=_("Use with caution."))

    class Meta:
        abstract = True

    def to_string(self):
        text = truncate_richtext_content(self.htmlblock)
        return text


class HtmlBlock(HtmlBlockBase):
    pass
