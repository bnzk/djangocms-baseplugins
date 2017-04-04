# coding: utf-8
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class HtmlBlockBase(AbstractBasePlugin):
    htmlblock = models.TextField(verbose_name=_("Html Block"), help_text=_("Use with caution."))

    class Meta:
        abstract = True

    def __str__(self):
        return u'HTML block'


class HtmlBlock(HtmlBlockBase):
    pass
