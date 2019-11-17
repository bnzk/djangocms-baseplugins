# coding: utf-8
from __future__ import unicode_literals

import datetime

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class AbstractBasePlugin(CMSPlugin):
    # text
    title = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name=_("Title"),
    )
    # visibility
    published = models.BooleanField(
        default=True,
        verbose_name=_("Published?"),
    )
    published_from_date = models.DateTimeField(
        null=True,
        default=None,
        blank=True,
        verbose_name=_("Published from"),
    )
    published_until_date = models.DateTimeField(
        null=True,
        default=None,
        blank=True,
        verbose_name=_("Published until"),
    )
    in_menu = models.BooleanField(
        default=False,
        verbose_name=_("In Menu?"),
    )
    # base opticss
    layout = models.CharField(
        max_length=64,
        default='',
        blank=True,
        verbose_name=_("Layout"),
    )
    background = models.CharField(
        max_length=64,
        blank=True,
        default='',
        verbose_name=_("Background"),
    )
    color = models.CharField(
        max_length=64,
        blank=True,
        default='',
        verbose_name=_("Color"),
    )
    # navigation
    anchor = models.SlugField(
        default='',
        blank=True,
        verbose_name=_("Anchor"),
    )

    class Meta:
        abstract = True

    # def __str__(self):
    #     return u'%s %s' % (self.__class__, self.get_hidden_flag())

    def __str__(self):
        if getattr(self, 'to_string'):
            return self.add_hidden_flag(self.to_string())
        else:
            return super(self.AbstractBasePlugin).__str__()

    # TODO: rename to is_published?
    def is_visible(self):
        if self.published:
            if self.published_from_date is None or \
                    self.published_from_date <= datetime.datetime.now():
                if self.published_until_date is None or \
                        self.published_until_date >= datetime.datetime.now():
                    return True
        return False

    def add_hidden_flag(self, text):
        return '{} {}'.format(text, self.get_hidden_flag())

    def get_hidden_flag(self):
        time_flag = ''
        if self.published_from_date:
            time_flag = '{}'.format(self.published_from_date)
            if not self.published_until_date:
                time_flag += ' - '
        if self.published_until_date:
            time_flag = '{} - {}'.format(time_flag, self.published_until_date)
        hidden_flag = ''
        if not self.published:
            hidden_flag = _('hidden')
        if hidden_flag and time_flag:
            return '({} / {})'.format(hidden_flag, time_flag)
        if hidden_flag or time_flag:
            return '({}{})'.format(hidden_flag, time_flag)
        return ''

    def get_plugin_css_block_class(self):
        return 'plugin-{}'.format(self.__class__.__name__.lower())

    # deprecate in 1.0!
    def get_css_classes(self):
        return self.css_classes

    @property
    def css_classes(self):
        plugin_block_class = self.get_plugin_css_block_class()
        classes = 'plugin plugin_{} '.format(self.pk)
        classes += ' {} '.format(plugin_block_class)
        if self.anchor:
            classes += ' plugin_{} '.format(self.anchor)
        classes += self._css_modifier_for_field('layout')
        classes += self._css_modifier_for_field('color')
        classes += self._css_modifier_for_field('background')
        classes += ' {}_position-{} '.format(plugin_block_class, self.position)
        if self.anchor:
            classes += ' {}_anchor-{} '.format(plugin_block_class, self.anchor)

        # deprecated for 1.0!
        classes += ' plugin_{}'.format(self.__class__.__name__.lower())
        classes += ' '.format(self.layout)
        classes += ' '.format(self.background)
        classes += ' '.format(self.color)
        return classes

    def _css_modifier_for_field(self, field):
        plugin_block_class = self.get_plugin_css_block_class()
        if getattr(self, field, None):
            return ' {}_{} '.format(plugin_block_class, getattr(self, field))
        return ''

    def get_anchor(self):
        """
        DEPRECATED:
        """
        if self.anchor:
            return "content-{}".format(self.anchor)
        if self.title:
            return "content-{}".format(slugify(self.title))
        return "content-{}".format(self.id)

    @property
    def html_id(self):
        if self.anchor:
            return "{}".format(self.anchor)
        if self.title:
            return "{}-{}".format(slugify(self.title), self.id)
        return "content-{}".format(self.id)

    @property
    def html_wrapper_attributes(self):
        attrs = self.html_wrapper_attributes_dict
        attrs_out = ''
        for attr_key, attr_value in attrs.items():
            attrs_out += ' {}="{}"'.format(attr_key, attr_value)
        return attrs_out

    @property
    def html_wrapper_attributes_dict(self):
        attrs = getattr(
            super(AbstractBasePlugin, self),
            'wrapper_attributes_dict',
            {}
        )
        my_attrs = {
            'class': self.css_classes,
            'id': self.html_id,
        }
        attrs.update(my_attrs)
        return attrs
