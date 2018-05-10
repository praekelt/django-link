from django.conf.urls import include, url
from django.contrib import admin

from link.tests import views


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^link/1/$", views.TestView.as_view(), name="link-1"),
    url(r"^link/2/$", views.TestView.as_view(), name="link-2"),
    url(r'^link/', include("link.urls", namespace="link"))
]
