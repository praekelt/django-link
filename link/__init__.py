from django.conf import settings


SETTINGS = getattr(settings, "LINK", {"excluded-viewname-choices": ["admin"]})
