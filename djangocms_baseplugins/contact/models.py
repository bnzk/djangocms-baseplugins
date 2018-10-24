# coding: utf-8
from __future__ import unicode_literals

import time

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
    address = models.TextField(_('Address'), default='', blank=True)
    geocoding_address = models.CharField(_('Address for the map'), max_length=64, default='', blank=True)

    lat = models.FloatField(blank=True, default=0, null=True)
    lng = models.FloatField(blank=True, default=0, null=True)
    geo_error = models.BooleanField(_("Probleme mit der Adresse?"), default=False)

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Contact / Subsidiary"))
        if self.geo_error:
            text = "%s (%s)" % (text, _("Coordinates Error!"))
        return self.add_hidden_flag(text)



class Contact(ContactBase):

    def save(self, *args, **kwargs):
        """
        here for now. may end in a metaclass, if we haz time to do this
        """
        try:
            import geocoder
        except:
            return super(Contact, self).save(*args, **kwargs)
        try:
            from_db = Contact.objects.get(id=self.id)
        except self.DoesNotExist:
            from_db = Contact()
        if self.geocoding_address:
            if not self.lat or not from_db.geocoding_address == self.geocoding_address:
                g = None
                try:
                    g = geocoder.komoot(self.geocoding_address)
                    time.sleep(2)
                except:
                    pass
                if g and g.ok:
                    self.lat = g.latlng[0]
                    self.lng = g.latlng[1]
                    self.geo_error = False
                else:
                    self.geo_error = True
            if not self.lat:
                # print "no latlng found: %s" % self
                self.geo_error = True
        else:
            self.geo_error = False
            self.lat = 0
            self.lng = 0

        return super(Contact, self).save(*args, **kwargs)
