# coding: utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content, sanitize_richtext
from djangocms_baseplugins.image.models import ImagePluginBase
from . import conf


@python_2_unicode_compatible
class TextImageBase(ImagePluginBase):
    body = RichTextField(_('Text'), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = truncate_richtext_content(self.body)
        return self.add_hidden_flag(text)

        def save(self, *args, **kwargs):
            if conf.TEXTPLUGIN_CLEAN_ON_SAVE:
                self.body = sanitize_richtext(self.body)
            super(TextImageBase, self).save(*args, **kwargs)


class TextImage(TextImageBase):
    pass
