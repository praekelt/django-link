from django import forms


from link.models import Link
from link.utils import get_view_names


class LinkAdminForm(forms.ModelForm):
    view_name = forms.ChoiceField(
        label="View Name",
        help_text="View name to which this link will redirect.",
        required=False
    )
    target = forms.ModelChoiceField(
        ModelBase.objects.all().order_by("title"),
        required=False,
        label="Target",
    )

    class Meta:
        model = Link
        fields = (
            "title", "subtitle", "view_name", "category", "target", "url"
        )

    def __init__(self, *args, **kwargs):
        # Set view_name choices to url pattern names
        view_name_choices = [("", "-- Select --"), ] + get_view_names()
        self.declared_fields["view_name"].choices = view_name_choices

        super(LinkAdminForm, self).__init__(*args, **kwargs)

        instance = kwargs.get("instance", None)
        if (instance is not None) and instance.target:
            self.fields["target"].initial = instance.target

    def clean(self):
        cleaned_data = super(LinkAdminForm, self).clean()
        fieldnames = ["view_name", "category", "target", "url"]
        for count, fieldname in enumerate(fieldnames):
            if cleaned_data[fieldname]:
                if count:
                    raise forms.ValidationError(
                        "You may set at most one of view_name, category, \
                        target or URL."
                    )
        return cleaned_data

    def _post_clean(self):
        super(LinkAdminForm, self)._post_clean()
        target = self.cleaned_data["target"]
        if target:
            self.instance.target_content_type = target.content_type
            self.instance.target_object_id = target.id
        else:
            self.instance.target_content_type = None
            self.instance.target_object_id = None
