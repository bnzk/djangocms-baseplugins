# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models.pluginmodel import CMSPlugin


class AbstractBasePlugin(CMSPlugin):
    # text
    title = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name=_("Title"),
    )
    # visibility
    published = models.BooleanField(
        default=True,
        verbose_name=_("Published?"),
    )
    in_menu = models.BooleanField(
        default=False,
        verbose_name=_("In Menu?"),
    )
    # base optics
    layout = models.CharField(
        max_length=64,
        default='',
        blank=True,
        verbose_name=_("Layout"),
    )
    background = models.CharField(
        max_length=64,
        blank=True,
        default='',
        verbose_name=_("Background"),
    )
    color = models.CharField(
        max_length=64,
        blank=True,
        default='',
        verbose_name=_("Color"),
    )
    # navigation
    anchor = models.SlugField(
        default='',
        blank=True,
        verbose_name=_("Anchor"),
    )

    class Meta:
        abstract = True

#    def __str__(self):
#        return u'%s %s' % (self.__class__, self.get_hidden_flag())

    def get_hidden_flag(self):
        hidden_flag = ''
        if not self.published:
            hidden_flag = '(%s)' % _('hidden')
        return hidden_flag