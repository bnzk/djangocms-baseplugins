from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import (
    check_migration_modules_needed,
    sanitize_richtext,
    truncate_richtext_content,
)

from . import conf

check_migration_modules_needed("text")


class TextBase(AbstractBasePlugin):
    body = RichTextField(_("Text"), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = truncate_richtext_content(self.body)
        return self.add_hidden_flag(text)

    def save(self, *args, **kwargs):
        if conf.CLEAN_ON_SAVE:
            self.body = sanitize_richtext(self.body)
        super(TextBase, self).save(*args, **kwargs)


class Text(TextBase):
    pass
