import requests
from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed
from djangocms_baseplugins.video import conf

if defaults.USE_FILER_ADDONS:
    from filer_addons.filer_gui.fields import FilerImageField
else:
    from filer.fields.image import FilerImageField


check_migration_modules_needed("video")


class VideoModelMixin(object):
    """
    needs "video_url" and "oembed_info" fields on model
    """

    def save(self):
        needs = False
        obj = None
        if self.id:
            obj = self.__class__.objects.filter(id=self.id).first()
            if obj and not obj.video_url == self.video_url:
                needs = True
        elif self.video_url:
            needs = True
        if needs:
            self.populate_oembed_infos()
        super().save()

    def populate_oembed_infos(self):
        if self.video_type == "youtube":
            url = "https://youtube.com/oembed/"
            params = {
                "format": "json",
                "url": self.video_url,
            }
        if self.video_type == "vimeo":
            url = "https://vimeo.com/api/oembed.json"
            params = {
                "url": self.video_url,
            }
        response = requests.get(url, params)
        if response.status_code == 200:
            self.oembed_info = response.json()

    def _set_base_infos(self):
        self._valid_url = False
        if self.video_url:
            for rule in conf.REGEXES:
                result, matches = rule.subn(self._repl, self.video_url)
                if matches:
                    vtype, vid = result.split("__ID_sep__", 1)
                    self._video_type = vtype
                    self._video_id = vid
                    self._valid_url = True
                    break

    def _repl(self, result):
        subgroups = result.groupdict()
        if subgroups.get("youtube_id", None):
            result = "youtube__ID_sep__%s" % subgroups["youtube_id"]
        elif subgroups.get("vimeo_id", None):
            result = "vimeo__ID_sep__%s" % subgroups["vimeo_id"]
        return result

    @property
    def aspect_ratio(self):
        if self.oembed_info.get("width", None) and self.oembed_info.get("height", None):
            return self.oembed_info["width"] / self.oembed_info["height"]
        return 0

    @property
    def video_type(self):
        if not getattr(self, "_video_type", None):
            self._set_base_infos()
        if self._valid_url:
            return self._video_type

    @property
    def video_id(self):
        if not getattr(self, "_video_id", None):
            self._set_base_infos()
        if self._valid_url:
            return self._video_id

    @property
    def embed_url_only(self):
        if self.video_type == "youtube":
            url = "https://www.youtube-nocookie.com/embed/%s?a=b" % (self.video_id,)
            return url
        if self.video_type == "vimeo":
            url = "https://player.vimeo.com/video/%s?a=b" % (self.video_id,)
            return url

    @property
    def embed_url_params(self):
        params = {}
        if self.video_type == "youtube":
            # https://developers.google.com/youtube/player_parameters
            if not getattr(self, "show_related", False):
                params["rel"] = "0"
            if not getattr(self, "fullscreen", True):
                params["fs"] = "0"
            if not getattr(self, "controls", True):
                params["controls"] = "0"
            if getattr(self, "autoplay", False):
                params["autoplay"] = "1"
            if not getattr(self, "infos", True):
                params["showinfo"] = "0"
            if conf.YOUTUBE_MODESTBRANDING:
                params["modestbranding"] = "1"
            if getattr(self, "mute", None) or params.get("autoplay"):
                params["mute"] = "1"
            params["color"] = conf.YOUTUBE_COLOR
        if self.video_type == "vimeo":
            # https://help.vimeo.com/hc/en-us/articles/12426260232977-Player-parameters-overview
            # https://player.vimeo.com/video/193349624?autoplay=1&loop=1&color=ff0b03&portrait=0
            if not getattr(self, "controls", True):
                params["controls"] = "0"
            if getattr(self, "autoplay", False):
                params["autoplay"] = "1"
            if not getattr(self, "infos", True):
                params["title"] = "0"
                params["byline"] = "0"
            if getattr(self, "mute", False) or params.get("autoplay"):
                params["muted"] = "1"
            if conf.VIMEO_COLOR:
                params["color"] = conf.VIDEOPLUGIN_VIMEO_COLOR
        return params

    @property
    def embed_url(self):
        url = self.embed_url_only
        params = self.embed_url_params
        for key, value in params.items():
            url += "&%s=%s" % (key, value)
            return url
        return url

    @property
    def video_preview_image(self):
        if getattr(self, "poster_image", None):
            return self.poster_image
        if self.video_type == "youtube":
            id = self.video_id
            # return 'https://i.ytimg.com/vi/%s/0.jpg' % yt_id
            # return 'https://img.youtube.com/vi/%s/maxresdefault.jpg' % yt_id
            return "https://img.youtube.com/vi/%s/0.jpg" % id
        if self.video_type == "vimeo":
            id = self.video_id
            return "https://vumbnail.com/%s.jpg" % id
        return ""


class VideoBase(VideoModelMixin, AbstractBasePlugin):
    video_url = models.URLField(  # noqa
        null=True,
        blank=True,
        verbose_name=_("Video Adresse"),
        help_text=_("youtube & vimeo"),
    )
    oembed_info = models.JSONField(
        default=dict,
        blank=True,
    )
    poster_image = FilerImageField(
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_image",
        blank=True,
        verbose_name=_("Poster Image"),
    )
    autoplay = models.BooleanField(
        default=False,
        verbose_name=_("Autoplay"),
        help_text=_("Enforces muting the video!"),
    )
    controls = models.BooleanField(
        default=True,
        verbose_name=_("show controls"),
        help_text=_("youtube only"),
    )
    infos = models.BooleanField(
        default=True,
        verbose_name=_("show infos"),
        help_text=_("not for youtube"),
    )
    fullscreen = models.BooleanField(
        default=True,
        verbose_name=_("allow fullscreen"),
    )
    show_related = models.BooleanField(
        default=False,
        verbose_name=_("show related"),
        help_text=_("youtube only"),
    )
    mute = models.BooleanField(
        default=False,
        verbose_name=_("mute"),
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = self.video_url
        return self.add_hidden_flag(text)


class Video(VideoBase):
    pass
