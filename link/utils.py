from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern


def get_view_names(view_names=[]):
    urlpatterns = __import__(settings.ROOT_URLCONF).urls.urlpatterns
    view_names = view_names or []
    for pattern in urlpatterns:
        if isinstance(pattern, RegexURLResolver):
            get_view_names(pattern.url_patterns, view_names)
        elif isinstance(pattern, RegexURLPattern):
            view_name = pattern.callback.func_name
            view_names.append(view_name)
    return view_names
