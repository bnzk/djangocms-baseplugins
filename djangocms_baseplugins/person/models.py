from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

if defaults.USE_FILER_ADDONS:
    from filer_addons.filer_gui.fields import FilerImageField
else:
    from filer.fields.image import FilerImageField


check_migration_modules_needed('person')


class PersonSectionBase(AbstractBasePlugin):
    class Meta:
        abstract = True

    def to_string(self):
        return str(_("People Section / Department"))


class PersonSection(PersonSectionBase):
    pass


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

    def to_string(self):
        text = u"%s %s" % (self.first_name, self.last_name)
        return text


class Person(PersonBase):
    pass
