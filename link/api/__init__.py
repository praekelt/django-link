from rest_framework import viewsets
from rest_framework import serializers

import rest_framework_extras

from link.models import Link


class PropertiesMixin(serializers.Serializer):
    absolute_url = serializers.ReadOnlyField()

    class Meta(object):
        fields = ("absolute_url", )


class LinkSerializer(PropertiesMixin, serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Link
        fields = ("absolute_url", )


class LinkObjectsViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


def register(router):
    return rest_framework_extras.register(
        router, (("link-link", LinkObjectsViewSet),)
    )
