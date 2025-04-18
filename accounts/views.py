from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from accounts.forms import CandidateRegistrationForm


class RegisterView(generic.CreateView):
    form_class = CandidateRegistrationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"


class SwitchRoleView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user = request.user

        if user.current_role == "candidate":
            user.current_role = "employer"
            messages.info(request, "Switched to Employer Mode")
        elif user.current_role == "employer":
            user.current_role = "candidate"
            messages.info(request, "Switched to Candidate Mode")

        user.save()

        return redirect("candidates:profile")
