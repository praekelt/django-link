from django.conf.urls import url

from link.views import LinkDetailView, LinkListView


urlpatterns = [
    url(r'^$', LinkListView.as_view(), name="link-list"),
    url(r'^(?P<slug>[-\w]+)/$', LinkDetailView.as_view(), name="link-detail")
]
