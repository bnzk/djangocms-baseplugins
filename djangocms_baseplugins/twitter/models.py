from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("twitter")


class TweetEmbedBase(AbstractBasePlugin):
    tweet_url = models.URLField(
        verbose_name=_("Tweet URL"),
        help_text=_(
            "Example: https://twitter.com/MdDoomFest/status/795834590481018880"
        ),
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = "%s" % (self.tweet_url)
        return self.add_hidden_flag(text)


class TweetEmbed(TweetEmbedBase):
    pass
