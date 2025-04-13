from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "website", "description"]
        widgets = {
            "description": CKEditorWidget(),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("This field cannot be empty.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if not description:
            raise forms.ValidationError("This field cannot be empty.")
        return description
