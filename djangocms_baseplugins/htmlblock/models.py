# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content


@python_2_unicode_compatible
class HtmlBlockBase(AbstractBasePlugin):
    htmlblock = models.TextField(verbose_name=_("HTML Block"), help_text=_("Use with caution."))

    class Meta:
        abstract = True

    def __str__(self):
        text = truncate_richtext_content(self.htmlblock)
        return self.add_hidden_flag(text)


class HtmlBlock(HtmlBlockBase):
    pass
