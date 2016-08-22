from django import forms


from link.models import Link
from link.utils import get_view_name_choices


class LinkAdminForm(forms.ModelForm):
    """
    Link admin class.
    """
    view_name = forms.ChoiceField(
        label="View Name",
        help_text="View name to which this link will redirect.",
        required=False
    )

    class Meta:
        model = Link

    def __init__(self, *args, **kwargs):
        """
        Set view_name choices to url pattern names.
        """
        view_name_choices = [("", "-- Select --"), ] + get_view_name_choices()
        self.declared_fields["view_name"].choices = view_name_choices
        super(LinkAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Adds validation to ensure that at least a view_name, target or url is
        selected.
        """
        cleaned_data = super(LinkAdminForm, self).clean()
        fieldnames = ["view_name", "target", "url"]
        for count, fieldname in enumerate(fieldnames):
            if cleaned_data[fieldname]:
                if count:
                    raise forms.ValidationError(
                        "You may set at most one of view_name, target or URL."
                    )
        return cleaned_data
