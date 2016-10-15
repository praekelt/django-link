from django import template

from link.models import Link

register = template.Library()


@register.inclusion_tag(
    "link/inclusion_tags/link_detail.html", takes_context=True
)
def render_link(context, slug):
    try:
        context["object"] = Link.objects.get(slug=slug)
    except Link.DoesNotExist:
        pass
    return context
