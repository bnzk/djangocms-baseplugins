# coding: utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content
from djangocms_baseplugins.image.models import ImageBase


@python_2_unicode_compatible
class TextImageBase(ImageBase):
    body = RichTextField(_('Text'), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = truncate_richtext_content(self.body)
        return self.add_hidden_flag(text)


class TextImage(TextImageBase):
    pass
