# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('loginform')


@python_2_unicode_compatible
class LoginForm(AbstractBasePlugin):

    def __str__(self):
        return self.add_hidden_flag(self.title)
