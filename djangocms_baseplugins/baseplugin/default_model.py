import datetime

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from . import defaults


class DefaultAbstractBasePlugin(CMSPlugin):
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
    size = models.CharField(
        max_length=64,
        blank=True,
        default='',
        verbose_name=_("Size"),
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
    custom = models.CharField(
        max_length=128,
        blank=True,
        default='',
        verbose_name=_("Custom"),
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
        if getattr(self, 'to_string', None):
            return self.add_hidden_flag(self.to_string())
        else:
            return super().__str__()

    # TODO: rename to is_published?
    def is_visible(self):
        if self.published:
            if self.published_from_date is None or \
                    self.published_from_date <= datetime.datetime.now():
                if self.published_until_date is None or \
                        self.published_until_date >= datetime.datetime.now():
                    return True
        return False

    def attrs_to_string(self, text, conf):
        if not conf.TO_STRING_ADD_ATTRS:
            return text
        for field in defaults.ATTR_FIELDS:
            if getattr(self, field, None):
                choices = getattr(conf, '{}_CHOICES'.format(field.upper()), [])
                for choice in choices:
                    if choice[0] == getattr(self, field, None):
                        text += ', ' if text else ''
                        text += str(choice[1])
        return text

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

    # deprecated, but why?
    def get_css_classes(self):
        print("DEPRECATED: BasePlugin.get css classes()")
        return self.css_classes()

    def css_classes(self):
        plugin_block_class = self.get_plugin_css_block_class()
        classes = 'plugin plugin_{} '.format(self.pk)
        classes += ' {} '.format(plugin_block_class)
        if self.anchor:
            classes += ' plugin_{} '.format(self.anchor)
        classes += self._css_modifier_for_field('layout')
        classes += self._css_modifier_for_field('size')
        classes += self._css_modifier_for_field('background')
        classes += self._css_modifier_for_field('color')
        classes += self._css_modifier_for_field('custom')
        classes += ' {}_position-{} '.format(plugin_block_class, self.position)
        if self.anchor:
            classes += ' {}_anchor-{} '.format(plugin_block_class, self.anchor)

        # deprecated for 1.0!
        classes += ' plugin_{}'.format(self.__class__.__name__.lower())
        # was dangerous! removed without deprecation
        # classes += ' {}'.format(self.layout)
        # classes += ' {}'.format(self.background)
        # classes += ' {}'.format(self.color)
        return classes

    def _css_modifier_for_field(self, field):
        plugin_block_class = self.get_plugin_css_block_class()
        if getattr(self, field, None):
            return ' {}_{} {}_{}-{}'.format(
                plugin_block_class,
                getattr(self, field),
                plugin_block_class,
                field,
                getattr(self, field),
            )
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

    def html_id(self):
        if self.anchor:
            return "{}".format(self.anchor)
        if self.title:
            return "{}-{}".format(slugify(self.title), self.id)
        return "content-{}".format(self.id)

    def html_wrapper_attributes(self):
        attrs = self.html_wrapper_attributes_dict()
        attrs_out = ''
        for attr_key, attr_value in attrs.items():
            attrs_out += ' {}="{}"'.format(attr_key, attr_value)
        return mark_safe(attrs_out)

    def html_wrapper_attributes_dict(self):
        attrs = getattr(
            super(),
            'wrapper_attributes_dict',
            {}
        )
        my_attrs = {
            'class': self.css_classes(),
            'id': self.html_id(),
        }
        attrs.update(my_attrs)
        return attrs
