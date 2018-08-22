# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class PersonSectionBase(AbstractBasePlugin):

    class Meta:
        abstract = True

    def __str__(self):
        return str(_("People Section / Department"))


class PersonSection(PersonSectionBase):
    pass


@python_2_unicode_compatible
class PersonBase(AbstractBasePlugin):
    image = FilerImageField(verbose_name=_("Image"), blank=True, null=True, default=None,
                            on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_image")
    salutation = models.CharField(_("Salutation"), blank=True, max_length=255, default='')
    function = models.CharField(_("Function"), blank=True, max_length=255, default='')
    department = models.CharField(_("Department"), blank=True, max_length=255, default='')
    first_name = models.CharField(_("First Name"), blank=True, max_length=255, default='')
    last_name = models.CharField(_("Last Name"), max_length=255, default='')
    body = RichTextField(_("Text"), blank=True, default='')
    email = models.EmailField(_("Email"), blank=True, default='')
    website = models.URLField(_("Website"), blank=True, default='')
    phone = models.CharField(_("Phone"), max_length=64, blank=True, default='')
    fax = models.CharField(_("Fax"), max_length=64, blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        text = u"%s %s" % (self.first_name, self.last_name)
        return self.add_hidden_flag(text)


class Person(PersonBase):
    pass
