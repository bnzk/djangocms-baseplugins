from django.db import models

from djangocms_baseplugins.baseplugin.default_model import DefaultAbstractBasePlugin


class InvalidAbstractBasePlugin(models.Model):
    class Meta:
        abstract = True


class CustomAbstractBasePlugin(DefaultAbstractBasePlugin):
    class Meta:
        abstract = True
