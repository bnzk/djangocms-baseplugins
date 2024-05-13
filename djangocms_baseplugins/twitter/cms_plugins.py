import requests
from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory

from . import conf
from .models import TweetEmbed

TweetEmbedPluginBase = baseplugin_classfactory(TweetEmbed, conf)


class TweetEmbedPlugin(TweetEmbedPluginBase):
    render_template = "djangocms_baseplugins/tweet_embed.html"

    def render(self, context, instance, placeholder):
        context = super(TweetEmbedPlugin, self).render(context, instance, placeholder)
        response = requests.get(
            "https://publish.twitter.com/oembed?url=%s" % instance.tweet_url
        )
        if response.status_code == 200:
            context.update(
                {
                    "embed": response.json(),
                }
            )
        return context


plugin_pool.register_plugin(TweetEmbedPlugin)
