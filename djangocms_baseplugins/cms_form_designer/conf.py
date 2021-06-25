import sys

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import get_baseplugin_fieldset, check_settings


# custom stuff, for form designer
TEMPLATESSETTING = True
CUSTOM_EMAIL_SEND = True

# basics
NAME = _('Form')
MODULE = defaults.SPECIAL_LABEL

# parent / children
ALLOW_CHILDREN = False
CHILD_CLASSES = []
REQUIRE_PARENT = False

# fields
TRANSLATED_FIELDS = []
CONTENT_FIELDS = ['form', 'text_intro', 'button_label', 'text_confirmation', ]

# choices
LAYOUT_CHOICES = (
    ('smalller', _("Kompakter"),),
    ('bigger', _("Umfangreicher"),),
)


# check for django settings that override!
check_settings('FORMDESIGNERPLUGIN', sys.modules[__name__], settings)

# define fieldsets! important: AFTER check_settings!
FIELDSETS = get_baseplugin_fieldset(**{
    'design': DESIGN_FIELDS,
    'content': CONTENT_FIELDS,
    'advanced': ADVANCED_FIELDS,
})


# OPPINIATED STUFF; MIGHT BE ADDED WITH A SETTINGS SWITCH ONE DAY
# FIELD_TYPES = []
# for item in BASE_FIELD_TYPES:
#     if not item.get('type', None) == 'multiple-select':
#         FIELD_TYPES.append(item)
#
#
# def disallow_is_required(field):
#     if field.is_required:
#         raise forms.ValidationError(
#             _("Sections and hidden fields cannot be required!")
#         )
#
#
# FIELD_TYPES.append({
#     "type": "section",
#     "verbose_name": _("Abschnitt"),
#     "field": partial(forms.CharField, widget=forms.HiddenInput, required=False),
#     "clean_field": [disallow_choices, disallow_is_required],
# })
