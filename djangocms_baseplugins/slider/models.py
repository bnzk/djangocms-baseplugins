from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class SliderBase(AbstractBasePlugin):
    height = models.CharField(_('Height'), max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Slider"))
        return self.add_hidden_flag(text)


class Slider(SliderBase):
    pass
