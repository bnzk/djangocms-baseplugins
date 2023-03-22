from cms.plugin_pool import plugin_pool

from djangocms_baseplugins.baseplugin.factory import baseplugin_formfactory, baseplugin_classfactory
from . import conf
from .models import Video


VideoPluginForm = baseplugin_formfactory(Video, conf)
VideoPlugin = baseplugin_classfactory(Video, conf, form=VideoPluginForm)
plugin_pool.register_plugin(VideoPlugin)


# class VideoPluginForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         exclude = []
#         widgets = get_baseplugin_widgets(conf)
#
#
# @plugin_pool.register_plugin
# class VideoPlugin(BasePluginMixin, CMSPluginBase):
#     model = Video
#     form = VideoPluginForm
#     module = defaults.CONTENT_LABEL
#     name = _(u'Video')
#     render_template = "djangocms_baseplugins/video.html"
#     fieldsets = conf.FIELDSETS
