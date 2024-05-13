from django import template

register = template.Library()


@register.filter()
def form_designer_pre_label_field(field):
    if field.field.widget.template_name.rsplit("/")[-1] in (
        "radio.html",
        "checkbox_select.html",
    ):
        return False
    return True
