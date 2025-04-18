from django import forms


class VacancySearchForm(forms.Form):
    text = forms.CharField(max_length=255, required=False)
