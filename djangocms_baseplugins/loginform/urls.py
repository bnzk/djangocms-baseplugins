from django.conf.urls import url

from .views import LoginFormView


urlpatterns = [
    url(r'^$', LoginFormView.as_view(), name='loginform'),
]
