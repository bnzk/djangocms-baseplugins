from django.shortcuts import redirect


class FormSentRedirectMiddleware(object):

    def __init__(self, get_response=None):
        if get_response:
            self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # none!

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return self.process_response(request, response)

    def process_response(self, request, response):
        # was it sent in the plugin code?!
        if getattr(request, 'form_designer_sent', False):
            return redirect('./?sent=true&id={}'.format(request.form_designer_sent))
        return response
