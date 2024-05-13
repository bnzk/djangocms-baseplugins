from cms.models import CMSPlugin, Placeholder


class BasePluginFormMixin(object):
    """
    mostly used when fine grained control of child plugins forms is needed
    - hide/show fields, based on parent plugin type/field values
    - different choices, based on parent plugin type/field values
    - same for placeholder slots
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = None
        self.placeholder = None
        if kwargs.get("initial", None):
            if kwargs["initial"].get("plugin_parent", None):
                self.parent = CMSPlugin.objects.get(
                    pk=kwargs["initial"]["plugin_parent"]
                )
            if kwargs["initial"].get("placeholder_id", None):
                self.placeholder = Placeholder.objects.get(
                    pk=kwargs["initial"]["placeholder_id"]
                )
        else:
            if self.instance.parent:
                parent_plugin = self.instance.parent
                self.parent, plugin = parent_plugin.get_plugin_instance()
            if self.instance.placeholder:
                self.placeholder = self.instance.placeholder
