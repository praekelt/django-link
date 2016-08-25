from django.conf import settings


SETTINGS = getattr(settings, "LINK", {"EXCLUDED_VIEWNAME_CHOICES": ["admin"]})
