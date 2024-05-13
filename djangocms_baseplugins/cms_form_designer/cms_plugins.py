import uuid

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.text import slugify

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin

from ..baseplugin.factory import baseplugin_formfactory
from . import conf
from .models import FormDefaultValue, FormDesigner
from .utils import check_form_send


class FormDefaultValueInline(admin.TabularInline):
    model = FormDefaultValue
    extra = 1


FormDesignerPluginForm = baseplugin_formfactory(FormDesigner, conf)


@plugin_pool.register_plugin
class FormDesignerPlugin(BasePluginMixin, CMSPluginBase):
    model = FormDesigner
    module = conf.MODULE
    name = conf.NAME
    cache = False
    form = FormDesignerPluginForm
    inlines = (FormDefaultValueInline,)
    render_template = "djangocms_baseplugins/form_designer.html"
    allow_children = conf.ALLOW_CHILDREN
    child_classes = conf.CHILD_CLASSES
    require_parent = conf.REQUIRE_PARENT
    fieldsets = conf.FIELDSETS

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context.get("request", None)
        # defaults
        initial = {}
        for default in instance.default_values.all():
            initial[slugify(default.field_name)] = slugify(default.default)
        # build form
        form_class = instance.form.form()
        form = None
        if request and request.method.lower() == "post":
            if request.POST.get("form_content_id", None) == str(instance.id):
                form = form_class(request.POST, initial=initial)
        if not form:
            form = form_class(initial=initial)
        sent = check_form_send(instance, request)
        if sent:
            # sent directly
            context["sent"] = True
            # if middleware is enabled, this causes the reidrect!
            request.form_designer_sent = instance.pk
            # if not, we dont get a redirect, and can submit the form again, with F5!
        elif (
            request
            and request.GET.get("sent", None)
            and request.GET.get("id", None) == str(instance.pk)
        ):
            # sent via app hook
            context["sent"] = True
        context["form"] = form
        context["submit_uuid"] = str(uuid.uuid1())
        return context
