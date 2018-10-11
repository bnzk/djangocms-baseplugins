# coding: utf-8
from __future__ import unicode_literals

from cms.models.fields import PageField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class ContentNavBase(AbstractBasePlugin):

    menu_depth = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Depth")
    )
    cms_page = PageField(
        default=None,
        help_text=_("Show submenu of this page")
    )
    sitemap = models.BooleanField(
        default=False,
        help_text=_("Show complete sitemap")
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Content Navigation"))
        return self.add_hidden_flag(text)


class ContentNav(ContentNavBase):
    pass
