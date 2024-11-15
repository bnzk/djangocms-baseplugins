import requests
from django.db import models

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed

check_migration_modules_needed("soundcloud")


class Soundcloud(AbstractBasePlugin):
    soundcloud_url = models.URLField()
    color = models.CharField(
        max_length=32,
        default="",
        blank=True,
    )
    autoplay = models.BooleanField(
        default=False,
    )
    show_comments = models.BooleanField(
        default=False,
    )

    def to_string(self):
        return "Soundcloud ({})".format(self.soundcloud_url)

    def get_oembed(self):
        """
        docs: https://developers.soundcloud.com/docs/oembed#introduction
        """
        url = "https://soundcloud.com/oembed"
        params = {
            "format": "json",
            "url": self.soundcloud_url,
            "maxheight": "166",
        }
        response = requests.get(url, params=params)
        return response.json()
