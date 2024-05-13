def check_form_send(plugin_instance, request):
    form_class = plugin_instance.form.form()
    # Standard form processing:
    if request and request.method.lower() == "post":
        form = form_class(request.POST)
        if form.is_valid():
            # run the configured processors:
            plugin_instance.form.process(form, request)
            return True
    return False
