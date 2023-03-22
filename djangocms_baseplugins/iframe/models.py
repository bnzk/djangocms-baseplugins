# coding: utf-8

from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed('iframe')


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
