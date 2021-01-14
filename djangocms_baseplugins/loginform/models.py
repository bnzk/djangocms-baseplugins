
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('loginform')


class LoginForm(AbstractBasePlugin):

    def __str__(self):
        return self.add_hidden_flag(self.title)
