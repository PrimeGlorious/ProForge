from django import forms
from ckeditor.widgets import CKEditorWidget

from candidates.models import Application
from employers.models import Company, Vacancy


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


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"
        widgets = {
            "description": CKEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.is_update = kwargs.pop("is_update", False)
        super().__init__(*args, **kwargs)


        if not self.is_update:
            self.fields["company"].queryset = Company.objects.filter(owner=self.user)
        else:
            self.fields.pop("company")


    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("This field cannot be empty.")
        return title

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")

        if salary is not None and salary < 0:
            raise forms.ValidationError("Salary must be a positive number.")

        return salary

    def clean_company(self):
        if self.is_update:
            return self.instance.company

        company = self.cleaned_data.get("company")
        if not company:
            raise forms.ValidationError("This field cannot be empty.")
        return company

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if not description:
            raise forms.ValidationError("This field cannot be empty.")
        return description


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["status"]
        widgets = {
            "status": forms.Select(choices=Application.Status.choices)
        }
