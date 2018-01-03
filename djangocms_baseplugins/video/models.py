# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from djangocms_baseplugins.baseplugin.utils import truncate_richtext_content
from djangocms_baseplugins.video import conf


@python_2_unicode_compatible
class VideoBase(AbstractBasePlugin):
    video_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('Video Adresse'),
        help_text=_('youtube & vimeo'),
    )
    autoplay = models.BooleanField(
        default=False,
        verbose_name=_('Autoplay'),
    )
    controls = models.BooleanField(
        default=True,
        verbose_name=_('show controls'),
        help_text=_('youtube only'),
    )
    infos = models.BooleanField(
        default=True,
        verbose_name=_('show infos'),
    )
    fullscreen = models.BooleanField(
        default=True,
        verbose_name=_('allow fullscreen'),
    )

    class Meta:
        abstract = True

    def __str__(self):
        text = self.video_url
        return self.add_hidden_flag(text)

    def _set_base_infos(self):
        self._valid_url = False
        if self.video_url:
            for rule in conf.VIDEOPLUGIN_REGEXES:
                result, matches = rule.subn(self._repl, self.video_url)
                if matches:
                    vtype, vid = result.split("__ID_sep__", 1)
                    self._video_type = vtype
                    self._video_id = vid
                    self._valid_url = True
                    break

    def _repl(self, result):
        subgroups = result.groupdict()
        if subgroups.get('youtube_id', None):
            result = 'youtube__ID_sep__%s' % subgroups['youtube_id']
        elif subgroups.get('vimeo_id', None):
            result = 'youtube__ID_sep__%s' % subgroups['vimeo_id']
        return result

    @property
    def video_type(self):
        if not getattr(self, '_video_type', None):
            self._set_base_infos()
        if self._valid_url:
            return self._video_type

    @property
    def video_id(self):
        if not getattr(self, '_video_id', None):
            self._set_base_infos()
        if self._valid_url:
            return self._video_id

    @property
    def embed_url(self):
        if self.video_type == 'youtube':
            return 'https://youtube.com/embed/%s' % self.video_id
        if self.video_type == 'vimeo':
            return 'https://vimeo.com/embed/%s' % self.video_id


class Video(VideoBase):
    pass
