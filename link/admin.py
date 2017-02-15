from django.contrib import admin

from link.forms import LinkAdminForm
from link.models import Link, ViewParam


class LinkAdmin(admin.ModelAdmin):
    form = LinkAdminForm
    list_display = ("title", "_get_absolute_url")
    prepopulated_fields = {"slug": ["title"]}
    filter_horizontal = ["view_params"]
    search_fields = [
        "title", "slug", "url"
    ]

    def _get_absolute_url(self, obj):
        url = obj.get_absolute_url()
        if url:
            return "<a href=\"%s\" target=\"public\">%s</a>" % (url, url)
        return "<p class=\"errornote\">Inactive or broken link</p>"

    _get_absolute_url.short_description = "Permalink"
    _get_absolute_url.allow_tags = True


admin.site.register(Link, LinkAdmin)
admin.site.register(ViewParam)
