from django import forms
from django.contrib.auth.forms import UserCreationForm

from candidates.models import Candidate


class CandidateRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Candidate
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")


class VacancySearchForm(forms.Form):
    text = forms.CharField(max_length=255, required=False)
