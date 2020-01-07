# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults as plugin_defaults, defaults
from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset
from .models import LoginForm


class LoginFormPlugin(BasePluginMixin, CMSPluginBase):
    model = LoginForm
    module = defaults.ADVANCED_LABEL
    name = _(u'Login Formular')
    render_template = "djangocms_baseplugins/loginform.html"
    fieldsets = get_baseplugin_fieldset(**{
        'design': [],
        'content': [],
        'advanced': plugin_defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
    cache = False

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
