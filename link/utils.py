from importlib import import_module

from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern

from link import SETTINGS


URLS = import_module(settings.ROOT_URLCONF).urlpatterns


def get_view_names(urlpatterns=URLS, view_names=[], namespace=None):
    if namespace not in SETTINGS.get("EXCLUDED_VIEWNAME_CHOICES", []):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver):
                get_view_names(
                    pattern.url_patterns, view_names, pattern.namespace
                )
            elif isinstance(pattern, RegexURLPattern):
                view_name = pattern.name
                if namespace:
                    view_name = "%s:%s" % (namespace, pattern.name)
                view_names.append(view_name)
    return view_names


def get_view_name_choices():
    return [tuple([view, view]) for view in get_view_names()]
