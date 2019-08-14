# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

# only when redirects are needed!
class LoginFormAppHook(CMSApp):
    name = _("LoginForm App")
    # menus = [CategoryMenu, ]
    urls = ["djangocms_loginform.urls", ]

apphook_pool.register(LoginFormAppHook)
