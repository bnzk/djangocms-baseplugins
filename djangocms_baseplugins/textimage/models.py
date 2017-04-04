# coding: utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from cms.models import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.utils.html import strip_tags
from django.utils.text import Truncator

from djangocms_baseplugins.image.models import ImageBase
from djangocms_baseplugins.text.models import TextBase


@python_2_unicode_compatible
class TextImageBase(ImageBase):
    body = RichTextField(_('Text'), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return Truncator(strip_tags(self.body).replace('&shy;', '')).words(3, truncate="...")


class TextImage(TextImageBase):
    pass
