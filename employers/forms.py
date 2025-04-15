from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Company, Vacancy


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
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields["company"].queryset = Company.objects.filter(owner=self.user)


    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("This field cannot be empty.")
        return title

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")

        if salary:
            if not isinstance(salary, int) or salary < 1:
                raise forms.ValidationError("Salary must be a positive integer.")

        return salary

    def clean_company(self):
        company = self.cleaned_data.get("company")
        if not company:
            raise forms.ValidationError("This field cannot be empty.")
        return company

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if not description:
            raise forms.ValidationError("This field cannot be empty.")
        return description
