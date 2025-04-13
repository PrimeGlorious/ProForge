from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CandidateRegistrationForm


class RegisterView(generic.CreateView):
    form_class = CandidateRegistrationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
