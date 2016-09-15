# djangocms-pluginbase
A common base for consistent djangocms plugin development. includes default plugins.

## Framework
Can be used as plugin framework, developping your own plugins. Features an astract base class, that provides the following:
- published field (and some logic in the render method), for easily hiding/showing content
- css_class field, used as "layout" field in most cases
- anchor_name field, when you need to access content directly via #hashbang
- some more

## Plugins included
All plugins have a abstract base class that can be used as starting point.

#### Containers
- Section, allows columns or other content within
- Column, used with a section
- Slider, a slider, defaults to owl-carousel2, but use what you want

#### Content
- Richtext, using django-ckeditor
- Image, using django-filer, simple one image displaying plugin
- Video, supports youtube and vimeo embeds
- Text and Image, for the case where you absolutely need them together
- Gallery, allowing multiple image plugins within
