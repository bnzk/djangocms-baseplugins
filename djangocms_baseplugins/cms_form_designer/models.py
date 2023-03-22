import json

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import format_html, mark_safe, strip_tags
from django.template.defaultfilters import linebreaksbr
from djangocms_baseplugins.baseplugin.models import AbstractBasePlugin
from django.core.mail import EmailMultiAlternatives
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.renderers import TemplatesSetting
from form_designer.models import Form, FormSubmission
from django import forms
from textblocks.templatetags.textblock_tags import textblock
from django.template.loader import render_to_string
from django.conf import settings

from djangocms_baseplugins.baseplugin.utils import check_migration_modules_needed


check_migration_modules_needed('cms_form_designer')


class FormDefaultValue(models.Model):
    plugin = models.ForeignKey(
        'cms_form_designer.FormDesigner',
        on_delete=models.CASCADE,
        related_name='default_values',
    )
    field_name = models.CharField(
        max_length=64,
    )
    default = models.CharField(
        max_length=64,
    )


class FormDesigner(AbstractBasePlugin):

    form = models.ForeignKey(
        'form_designer.Form',
        on_delete=models.PROTECT,
        null=True,
    )
    text_intro = RichTextField(
        default='',
        blank=True,
        help_text='Shown initially, above the form. If empty, nothing is shown'
    )
    text_confirmation = RichTextField(
        default='',
        blank=True,
        help_text='Shown after form was sent. If empty, a fallback is shown'
    )
    button_label = models.CharField(
        max_length=64,
        default='',
        blank=True,
        help_text='Text for the form send button'
    )

    def to_string(self):
        if self.form and self.form.title:
            text = self.form.title
        else:
            text = self.title
        return text

    def copy_relations(self, old_instance):
        super().copy_relations(old_instance)
        for entry in old_instance.default_values.all():
            entry.id = None
            entry.save()
            self.default_values.add(entry)


def send_emails(model_instance, form_instance, request, config, **kwargs):
    submission = FormSubmission(
        form=model_instance,
        data=json.dumps(form_instance.cleaned_data, cls=DjangoJSONEncoder),
        path=request.path,
    )
    cleaned = form_instance.cleaned_data
    headers = {}
    sender = None
    if config.get('sender_field', None):
        sender = cleaned.get(config.get('sender_field'), '')
        if sender:
            headers = {
                'Reply-To': sender
            }
    # to recipient, in any case
    send_to = [email.strip() for email in config["recipients"].split(",")]
    msg = EmailMultiAlternatives(
        model_instance.title,
        custom_formatted_data(submission),
        to=send_to,
        from_email=settings.DEFAULT_FROM_EMAIL,
        headers=headers,
    )
    html = render_to_string(
        'cms_form_designer/emails/recipient.html',
        {'body': custom_formatted_data(submission, html=True)}
    )
    msg.attach_alternative(html, "text/html")
    msg.send(fail_silently=False)
    # copy
    if sender:
        copy_subject = '{}{}'.format(
            textblock("Bestätigung - ", help_text="Formular Email Subject Prefix für sender Kopie"),
            model_instance.title,
        )
        copy_body = textblock(
            "Vielen Dank! ... ",
            type="text/html",
            help_text="Formular Email Body für sender Kopie"
        )
        copy_html = render_to_string(
            'cms_form_designer/emails/confirmation.html', {'body': copy_body}
        )
        msg = EmailMultiAlternatives(
            copy_subject,
            strip_tags(copy_body),
            to=[sender, ],
            from_email=settings.DEFAULT_FROM_EMAIL,
        )
        msg.attach_alternative(copy_html, "text/html")
        msg.send(fail_silently=False)
    return True


def custom_formatted_data(submission, html=False):
    data_dict = json.loads(submission.data)
    out = ""
    for field in submission.form.fields.all():
        value = data_dict.get(field.name)
        title = field.title
        if field.type == 'longtext':
            value = linebreaksbr(value)
        out += custom_data_row(title, value, html)
    # out += custom_data_row('Submitted', submission.submitted, html)
    out += custom_data_row('Path', submission.path, html)
    return mark_safe(out)


def custom_data_row(title, value, html=False):
    if html:
        return format_html('<b>{}</b><br>{}<br><br>', title, value)
    else:
        return "{}: {}\n".format(title, value)


# def validate_send_emails(form_instance, data):
#     print("123")
#     if data.get('copy_to_sender', None):
#         print("ssss123")
#         if not data.get('sender_field', None):
#             print("sssdsvadsvadvasdv123")
#             raise ValidationError('sender field required, when sending a copy')
#     return data


Form.CONFIG_OPTIONS[1] = (
    "send_emails",
    {
        "title": ("Email schicken"),
        "form_fields": [
            ("recipients", forms.CharField(
                label=("Empfänger Email"),
                required=True,
                # validators...
                help_text="Feld, welches die Email Adresse enthält"
            )),
            ("copy_to_sender", forms.BooleanField(
                label=("Send copy to sender"),
                required=False,
                # validators...
                help_text="Kopie an den Absender schicken?"
            )),
            ("sender_field", forms.CharField(
                label=("Sender E-Mail field"),
                required=False,
                # validators...
                help_text="Feld, welches die Email Adresse enthält"
            )),
        ],
        "process": send_emails,
        # "validate": validate_send_emails,
    }
)


def form_class(self):
    cls = self.orig_form_class()
    cls.default_renderer = TemplatesSetting()
    return cls


# prevent endless loop when reloading things during tests, or elsewhere
if not getattr(Form, 'form_class_patched', None):
    Form.form_class_patched = True
    Form.orig_form_class = Form.form_class
    Form.form_class = form_class
