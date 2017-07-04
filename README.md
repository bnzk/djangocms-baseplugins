djangocms-baseplugins
=====================

.. image:: https://travis-ci.org/bnzk/djangocms-baseplugins.svg
    :target: https://travis-ci.org/bnzk/djangocms-baseplugins/
.. image:: https://img.shields.io/pypi/v/djangocms-baseplugins.svg
    :target: https://pypi.python.org/pypi/djangocms-baseplugins/
.. image:: https://img.shields.io/pypi/l/djangocms-baseplugins.svg
    :target: https://pypi.python.org/pypi/djangocms-baseplugins/

A common base for consistent djangocms plugin development. includes default plugins.


Framework
---------

Can be used as plugin framework, developping your own plugins. Features an astract base class, that provides the following:
- **published** field (and some logic in the render method), for easily hiding/showing content
- **css_class** field, used as "layout" field in most cases
- **anchor_name** field, when you need to access content directly via #hashbang
- **some** more

Plugins included
----------------

All plugins have a abstract base class that can be used as starting point.

#### Containers
- **[Section](#section)**, allows columns or other content within
- **Column**, used with a section
- **Slider**, a slider, defaults to owl-carousel2, but use what you want

#### Content
- **Richtext**, using django-ckeditor
- **Image**, using django-filer, simple one image displaying plugin
- **Video**, supports youtube and vimeo embeds
- **Text** and Image, for the case where you absolutely need them together
- **Gallery**, allowing multiple image plugins within


# Plugin Docs


## General

All plugins share the same settings model:

    WHATEVERPLUGIN_CONTENT_FIELDS (default: title)
    WHATEVERPLUGIN_DESIGN_FIELDS (default: layout)
    WHATEVERPLUGIN_FIELDSETS (default: builds a fieldset with CONTENT_FIELDS, DESIGN_FIELDS and BASEPLUGIN_ADVANCED_FIELDS)
    WHATEVERPLUGIN_WHATEVERSETTING

For container plugins:

    WHATEVERPLUGIN_CHILD_CLASSES (default: depends on container)

You can easily find out about the settings available: Browse below, or have a look at the djangocms_baseplugins/whateverplugin/conf.py


## Containers

Container plugins are made to be containers for other plugins. Be it just for defining sections, be it for defining
sections with X columns, be it for defining a slider.


### Section

Section container.

#### Settings

    SECTIONPLUGIN_CHILD_CLASSES (default: ColumnPlugin)


### Column

### Slider

## Content Plugins

### Text

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


### Image

