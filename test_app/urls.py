"""URLs to run the tests."""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import static

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += i18n_patterns(
    path("", include("cms.urls")),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            static.serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]
