# coding: utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class ContactBase(AbstractBasePlugin):
    website = models.URLField(_("Website"), blank=True, default='')
    email = models.EmailField(_("Email"), blank=True, default='')
    phone = models.CharField(_("Phone"), max_length=64, blank=True, default='')
    fax = models.CharField(_("Fax"), max_length=64, blank=True, default='')
    body = RichTextField(_("Text"), blank=True, default='')
    address = models.CharField(_('Address'), max_length=512, default='', blank=True)
    geocoding_address = models.CharField(_('Address for the map'), max_length=64, default='', blank=True)


    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Contact / Subsidiary"))
        return self.add_hidden_flag(text)


class Contact(ContactBase):
    pass
