from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CandidateRegistrationForm


class RegisterView(generic.CreateView):
    form_class = CandidateRegistrationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"


def switch_role(request: HttpRequest) -> HttpResponse:
    user = request.user

    if user.current_role == "C":
        user.current_role = "E"
        messages.info(request, "Switched to Employer Mode")
    elif user.current_role == "E":
        user.current_role = "C"
        messages.info(request, "Switched to Candidate Mode")

    user.save()

    return redirect('candidates:profile')
