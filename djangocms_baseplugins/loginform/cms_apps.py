# coding: utf-8
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


# only when redirects are needed!
@apphook_pool.register
class LoginFormAppHook(CMSApp):
    name = _("LoginForm App")
    urls = ["djangocms_loginform.urls", ]
    # menus = [CategoryMenu, ]
