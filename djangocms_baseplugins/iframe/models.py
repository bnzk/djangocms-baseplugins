# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


class IframeBase(models.Model):
    """
    abstract base model, no cmsplugin mixed in
    """
    iframe_url = models.CharField(
        max_length=1024,
        default='',
        blank=False,
        verbose_name=_('URL')
    )

    class Meta:
        abstract = True

    def to_string(self):
        text = ''
        if self.iframe_url:
            text = self.iframe_url
        return text


class Iframe(AbstractBasePlugin, IframeBase):
    pass
