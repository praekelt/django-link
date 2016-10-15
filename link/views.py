from django.views import generic

from link.models import Link


class LinkDetailView(generic.detail.DetailView):
    model = Link
    template = "link/link_detail.html"


class LinkListView(generic.list.ListView):
    model = Link
    template = "link/link_list.html"
