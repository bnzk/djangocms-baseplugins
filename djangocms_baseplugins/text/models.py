# coding: utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content, sanitize_richtext
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed
from . import conf


check_migration_modules_needed('text')


@python_2_unicode_compatible
class TextBase(AbstractBasePlugin):
    body = RichTextField(_('Text'), blank=True)

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
