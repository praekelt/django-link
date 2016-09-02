from django.contrib import admin

from link.forms import LinkAdminForm
from link.models import Link, ViewParam


class LinkAdmin(admin.ModelAdmin):
    form = LinkAdminForm
    list_display = ("title", "_get_absolute_url")
    prepopulated_fields = {"slug": ["title"]}

    def _get_absolute_url(self, obj):
        url = obj.get_absolute_url()
        return "<a href=\"%s\" target=\"public\">%s</a>" % (url, url)

    _get_absolute_url.short_description = "Permalink"
    _get_absolute_url.allow_tags = True


admin.site.register(Link, LinkAdmin)
admin.site.register(ViewParam)
