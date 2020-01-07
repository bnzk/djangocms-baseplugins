# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin

if defaults.USE_FILER_ADDONS:
    from filer_addons.filer_gui.fields import FilerImageField
else:
    from filer.fields.image import FilerImageField


class IframeBase(models.Model):
    """
    abstract base model, no cmsplugin mixed in
    """
    image = FilerImageField(
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_iframe",
        verbose_name=_("Iframe"),
    )
    caption = models.CharField(
        max_length=255,
        default='',
        blank=True,
    )

    class Meta:
        abstract = True

    def to_string(self):
        text = ''
        if self.caption:
            text = '%s, %s' % (self.caption, self.iframe)
        if self.alt_text:
            text = '%s, %s' % (self.alt_text, self.iframe)
        if not text:
            text = '%s' % (self.iframe)
        return text


class Iframe(AbstractBasePlugin, IframeBase):
    pass