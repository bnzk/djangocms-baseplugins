# form_designer django-cms plugin

integrates `form_designer` with `django-cms`. 

## setup

add `form_desinger` to your requirements.txt, or whatever file you use 
to track your dependencies.

installed apps, add

```
...
# adds plugin models and plugins itself
'djangocms_baseplugins.cms_form_designer',

# optional, enables more export options in admin, uses django-admin-sort for inline sorting
'djangocms_baseplugins.cms_form_designer.admin_overrides',  
...
```

middleware, add:

    'djangocms_form_designer.middleware.FormSentRedirectMiddleware',

## configuration

all the default baseplugins settings apply. besides that:

`FORMDESIGNERPLUGIN_TEMPLATESSETTING (False)` use TemplatesSetting as default renderer
on all forms. Read more here: https://docs.djangoproject.com/en/3.1/ref/forms/renderers/#templatessetting . 
Needs `django.forms` in `INSTALLED_APPS`. Enables more control how widgets and labels are rendered,
usefull when doing advanced custom CSS styled radios/checkboxes/selects. Hint: label position in html.

`FORMDESIGNERPLUGIN_CUSTOM_EMAIL_SEND (True)` use an alternate sending mechanism (copy to sender, etc)
instead of the orginal one. See `models.py` for details.

## notes

- needs `django-textblocks` as a dependency, for subject, confirmation, and other texts
  would probably possible without (with a setting), but we don't have the time for it right now.
- `djangocms_baseplugins.cms_form_designer.admin_overrides` needs `django-admin-sort` as a dependency, 
  for inline ordering. as I never got the original inline ordering working (django-order, I think)
- one day, add the possibility to translate forms via modeltranslation, with an additional sub-app
