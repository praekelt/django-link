DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

ROOT_URLCONF = "link.tests.urls"

INSTALLED_APPS = (
    "test_without_migrations",
    "link",
    "django.contrib.contenttypes",
    "django.contrib.sites",
)

SITE_ID = 1

SECRET_KEY = "SECRET_KEY"
