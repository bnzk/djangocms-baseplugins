# coding: utf-8
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content


@python_2_unicode_compatible
class TextBase(AbstractBasePlugin):
    body = RichTextField(_('text'), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return truncate_richtext_content(self.body)


class Text(TextBase):
    pass
