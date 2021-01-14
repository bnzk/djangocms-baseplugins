# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_widgets
from . import conf
from .models import LoginForm


class LoginFormPluginForm(forms.ModelForm):
    class Meta:
        model = LoginForm
        exclude = []
        widgets = get_baseplugin_widgets(conf)


class LoginFormPlugin(BasePluginMixin, CMSPluginBase):
    form = LoginFormPluginForm
    model = LoginForm
    module = conf.MODULE
    name = conf.NAME
    render_template = "djangocms_baseplugins/loginform.html"
    fieldsets = conf.FIELDSETS
    cache = False
    allow_children = conf.ALLOW_CHILDREN
    child_classes = conf.CHILD_CLASSES
    require_parent = conf.REQUIRE_PARENT

    def render(self, context, instance, placeholder):
        context = super(LoginFormPlugin, self).render(context, instance, placeholder)
        request = context['request']
        context['login_form'] = check_for_login_form(request)
        return context


plugin_pool.register_plugin(LoginFormPlugin)


def check_for_login_form(request):
    form = None
    if not request.user.is_authenticated():
        if (request.method == 'POST'):
            form = AuthenticationForm(request, request.POST)
            # checks auth!
            if form.is_valid() and form.user_cache:
                login(request, form.user_cache)
                form = None
        else:
            form = AuthenticationForm(request)
    return form
