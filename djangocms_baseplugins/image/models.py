# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from .base import ImagePluginBase


class Image(ImagePluginBase):
    pass
