from django.shortcuts import redirect
from django.views.generic import TemplateView

from .cms_plugins import check_for_login_form


class LoginFormView(TemplateView):
    template_name = "djangocms_baseplugins/loginform.html"

    def dispatch(self, request, *args, **kwargs):
        self.form = check_for_login_form(request)
        if (
            request.method == "POST"
            and request.user.is_authenticated
            and request.GET.get("next", None)
        ):
            return redirect(request.GET.get("next"))
        return super(LoginFormView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
