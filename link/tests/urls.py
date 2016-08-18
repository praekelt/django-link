from django.conf.urls import url

from link.tests import views


urlpatterns = [
    url(
        r"^link/1/$", views.TestView.as_view(), name="link-1"
    ),
    url(
        r"^link/2/$", views.TestView.as_view(), name="link-2"
    ),
]
