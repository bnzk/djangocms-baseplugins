from django.urls import path

from .views import LoginFormView

urlpatterns = [
    path("", LoginFormView.as_view(), name="loginform"),
]
