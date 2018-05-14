# djangocms-baseplugins

[![Build Status](https://travis-ci.org/bnzk/djangocms-baseplugins.svg "Build Status")](https://travis-ci.org/bnzk/djangocms-baseplugins/)
[![PyPi Version](https://img.shields.io/pypi/v/djangocms-baseplugins.svg "PyPi Version")](https://pypi.python.org/pypi/djangocms-baseplugins/)
[![Licence](https://img.shields.io/pypi/l/djangocms-baseplugins.svg "Licence")](https://pypi.python.org/pypi/djangocms-baseplugins/)

A common base for consistent djangocms plugin development. includes default plugins.


## Framework

Can be used as plugin framework, developping your own plugins. Features an astract base class, that provides the following:
- **published** field (and some logic in the render method), for easily hiding/showing content
- **css_class** field, used as "layout" field in most cases
- **anchor_name** field, when you need to access content directly via #hashbang
- **some** more

## Plugins included

### Containers

- **[Section](#section)**, allows columns or other content within
- **Column**, used with a section
- **Slider**, a slider, defaults to owl-carousel2 (not yet there is any js..), but use what you want

### Content

- **Richtext**, using django-ckeditor
- **Image**, using django-filer, simple one image displaying plugin
- **TextImage**, using django-filer, combine text & image, if you have to
- **Video**, supports youtube and vimeo embeds
- **Gallery**, allowing multiple image plugins within


## Setting up / using it

### Settings

#### General

**DJANGOCMS_BASEPLUGINS_ADVANCED_LABEL** text (in locale) used to label advanced plugins (module attribute of CMSPlugin). defaults to _("z Advanced").

**DJANGOCMS_BASEPLUGINS_CONTENT_LABEL** same for normal content. defaults to _("Content")

**DJANGOCMS_BASEPLUGINS_CONTAINER_LABEL** same for container plugins. defaults to _("Containers")

**DJANGOCMS_BASEPLUGINS_MODE** some pre-configuration for fields and fieldsets. defaults to 'default'. possible options are 'full', 'minimal' and 'default'. depending on this setting, more or less advanced fields are shown.

**BASEPLUGIN_ADVANCED_FIELDS** own configuration of fields to be shown in the advanced fieldset. if not set, based on `DJANGOCMS_BASEPLUGINS_MODE`.

**WIDTH_CHOICES** width choices, used where widhts are needed. defaults to

    ('', _('Automatic')),
    ('w-100', _('100%')),
    ('w-66', _('66%')),
    ('w-50', _('50%')),
    ('w-33', _('33%')),


#### Per plugin type settings

All plugins share the same settings concept:


    WHATEVERPLUGIN_CONTENT_FIELDS (default: title)
    WHATEVERPLUGIN_DESIGN_FIELDS (default: layout)
    WHATEVERPLUGIN_FIELDSETS (default: builds a fieldset with CONTENT_FIELDS, DESIGN_FIELDS and BASEPLUGIN_ADVANCED_FIELDS)
    WHATEVERPLUGIN_WHATEVERSETTING

For container plugins:

.. code-block:: python

    WHATEVERPLUGIN_CHILD_CLASSES (default depends on container)

You can easily find out about the settings available: Browse below, or have a look at the djangocms_baseplugins/whateverplugin/conf.py




### Container plugins

Container plugins are made to be containers for other plugins. Be it just for defining sections, be it for defining
sections with X columns, be it for defining a slider.


#### Section

Section container.

**Settings**

    SECTIONPLUGIN_CHILD_CLASSES (default: ColumnPlugin)


#### Column


#### Slider


### Content Plugins

#### Text

Simple Textplugin, using ckeditor. Obviously, adds django-ckeditor as dependency.

Use `CKEDITOR_SETTINGS` for configuring your ckeditor. For example, a rather simple one:


    CKEDITOR_SETTINGS = {
        'toolbar': 'MINE',
        'toolbar_MINE': [
            ['Undo', 'Redo'],
            ['Link', 'Unlink', ],
            ['Bold', 'RemoveFormat', ],
            ['Format'],
            ['Cut', 'Copy', 'PasteText', ],
            ['cleanup', ],
            ['ShowBlocks', 'Source'],
        ],
        'format_tags': 'h1;h2;h3;p',
        'skin': 'moono',
    }

#### Image

Image plugin. Reference one image, with a django-filer FilerImageField, add caption and alt text.
