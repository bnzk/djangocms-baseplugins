# coding: utf-8
import requests
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import TweetEmbed
from . import conf


class TweetEmbedPlugin(BasePluginMixin, CMSPluginBase):
    model = TweetEmbed
    name = _(u'twitter')
    render_template = "twitter/tweet_embed.html"
    fieldsets = conf.TWEETEMBEDPLUGIN_FIELDSETS

    def render(self, context, instance, placeholder):
        context = super(TweetEmbedPlugin, self).render(context, instance, placeholder)
        response = requests.get("https://publish.twitter.com/oembed?url=%s" % instance.tweet_url)
        if response.status_code == 200:
            context.update({'embed': response.json(), })
        return context


plugin_pool.register_plugin(TweetEmbedPlugin)
