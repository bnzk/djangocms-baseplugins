# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('twitter')


@python_2_unicode_compatible
class TweetEmbedBase(AbstractBasePlugin):
    tweet_url = models.URLField(
        verbose_name=_("Tweet URL"),
        help_text=_("Example: https://twitter.com/MdDoomFest/status/795834590481018880"),
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = u'%s' % (self.tweet_url)
        return self.add_hidden_flag(text)


class TweetEmbed(TweetEmbedBase):
    pass
