# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin


@python_2_unicode_compatible
class TeaserSectionBase(AbstractBasePlugin):
    class Meta:
        abstract = True

    def __str__(self):
        text = str(_("Teaser Section"))
        return self.add_hidden_flag(text)


class TeaserSection(TeaserSectionBase):
    pass
