from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
try:
    from django.urls import reverse, NoReverseMatch
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch

class ViewParam(models.Model):
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=256)

    class Meta:
        ordering = ["key"]

    def __unicode__(self):
        return "%s:%s" % (self.key, self.value)

    __str__ = __unicode__


class Link(models.Model):
    title = models.CharField(
        max_length=256,
        help_text="A short descriptive title."
    )
    slug = models.SlugField(
        max_length=256,
        db_index=True,
    )
    view_name = models.CharField(
        max_length=256, blank=True, null=True,
        help_text="View name to which this link will redirect."
    )
    view_params = models.ManyToManyField(
        ViewParam, blank=True, null=True
    )
    target_content_type = models.ForeignKey(
        ContentType, blank=True, null=True,
        related_name="link_target_content_type",
        on_delete=models.CASCADE
    )
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey("target_content_type", "target_object_id")
    url = models.CharField(
        max_length=256, blank=True, null=True,
        help_text="URL to which this link will redirect."
    )

    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title

    __str__ = __unicode__

    @property
    def absolute_url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        """
        Returns URL to which link should redirect based on a reversed view
        name, category, target or explicitly provided URL.
        """
        if self.view_name:
            kwargs = dict(
                (param.key, param.value) for param in self.view_params.all()
            )
            try:
                return reverse(self.view_name, kwargs=kwargs)
            except NoReverseMatch:
                pass
        elif self.target:
            try:
                return self.target.get_absolute_url()
            except AttributeError:
                pass
        else:
            # Django can be served in a subdirectory. Transparently fix urls.
            if "://" in self.url:
                return self.url

            # Urls not starting with a slash probably do so with reason. Skip.
            if not self.url.startswith("/"):
                return self.url

            # Request is not available here so use reverse to determine root
            try:
                root = reverse("home")
            except NoReverseMatch:
                return self.url

            # /abc and /root/abc must be transformed into /root/abc
            if not self.url.startswith(root):
                return root.rstrip("/") + "/" + self.url.lstrip("/")

        return self.url
