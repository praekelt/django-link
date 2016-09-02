from rest_framework import viewsets
from rest_framework import serializers

import djangorestframework_extras

from link.models import Link


class PropertiesMixin(serializers.Serializer):
    absolute_url = ReadOnlyField()

    class Meta:
        fields = ("absolute_url")


class LinkSerializer(
    PropertiesMixin, serializers.HyperlinkedModelSerializer
    ):

    # xxx: meta may need to be Meta(serializers.HyperlinkedModelSerializer)
    class Meta:
        model = Link


class LinkObjectsViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


def register(router):
    return djangorestframework_extras.register(
        router,
        (
            ("link-link", LinkObjectsViewSet)
        )
    )
