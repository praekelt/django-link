from django import forms


from link.models import Link
from link.utils import get_view_name_choices


class LinkAdminForm(forms.ModelForm):
    view_name = forms.ChoiceField(required=False)

    class Meta:
        model = Link
        fields = [
            "title", "slug", "view_name", "view_params", "target_content_type",
            "target_object_id", "url"
        ]

    def __init__(self, *args, **kwargs):
        """
        Set view_name choices to the availbale url pattern names.
        """
        view_name_choices = [("", "-- Select --"), ] + get_view_name_choices()
        self.declared_fields["view_name"].choices = view_name_choices

        super(LinkAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Adds validation to ensure that only one view_name, target or url is
        selected.
        """
        cleaned_data = super(LinkAdminForm, self).clean()
        field_count = 0
        for fieldname in ["view_name", "target_content_type", "url"]:
            if cleaned_data[fieldname]:
                if field_count:
                    raise forms.ValidationError(
                        "You may set at most one of view_name, target or URL."
                    )
                field_count += 1

        if not field_count:
            raise forms.ValidationError(
                "You may set at least one of view_name, target or URL."
            )

        return cleaned_data
