# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.db import models
from cms.models.pluginmodel import CMSPlugin


class AbstractBasePlugin(CMSPlugin):
    # text
    title = models.CharField(max_length=256, blank=True, default='')
    # visibility
    published = models.BooleanField(default=True)
    in_menu = models.BooleanField(default=False)
    # base optics
    layout = models.CharField(max_length=64, default='')
    background = models.CharField(max_length=64, default='')
    color = models.CharField(max_length=64, default='')
    # navigation
    anchor = models.SlugField(blank=True, default='')

    class Meta:
        abstract = True

#    def __str__(self):
#        return u'%s %s' % (self.__class__, self.get_hidden_flag())

    def get_hidden_flag(self):
        hidden_flag = ''
        if not self.published:
            hidden_flag = '(%s)' % _('hidden')
        return hidden_flag