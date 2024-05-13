from cms.plugin_pool import plugin_pool
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from djangocms_baseplugins.baseplugin.factory import baseplugin_classfactory

from . import conf
from .models import LoginForm

LoginFormPluginBase = baseplugin_classfactory(LoginForm, conf)


class LoginFormPlugin(LoginFormPluginBase):
    def render(self, context, instance, placeholder):
        context = super(LoginFormPlugin, self).render(context, instance, placeholder)
        request = context["request"]
        context["login_form"] = check_for_login_form(request)
        return context


plugin_pool.register_plugin(LoginFormPlugin)


def check_for_login_form(request):
    form = None
    if not request.user.is_authenticated():
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            # checks auth!
            if form.is_valid() and form.user_cache:
                login(request, form.user_cache)
                form = None
        else:
            form = AuthenticationForm(request)
    return form
