from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView

from candidates.models import Vacancy
from employers.models import Company


class IndexView(TemplateView):
    template_name = "candidates/index.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        vacancies_count = Vacancy.objects.count()
        companies_count = Company.objects.count()
        candidates_count = get_user_model().objects.count()
        context = {
            "vacancies_count": vacancies_count,
            "companies_count": companies_count,
            "candidates_count": candidates_count,
        }
        return render(request, self.template_name, context=context)


class AboutView(TemplateView):
    template_name = "candidates/about.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name)


class ProfileView(TemplateView):
    template_name = "candidates/profile.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        current_user = request.user

        applications = current_user.applications.all().order_by("-created_at")
        vacancies_count = Vacancy.objects.filter(company__owner=current_user).count()

        context = {
            "applications": applications,
            "current_user": current_user,
            "vacancies_count": vacancies_count
        }

        return render(request, self.template_name, context=context)


class ApplyView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        vacancy = get_object_or_404(Vacancy, id=pk)

        if vacancy in request.user.vacancies.all():
            request.user.vacancies.remove(vacancy)
        else:
            request.user.vacancies.add(vacancy)

        return redirect(reverse("employers:vacancies_detail", args=[pk]))


class ToggleSaveVacancyView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        vacancy = get_object_or_404(Vacancy, id=pk)

        if vacancy in request.user.saved_vacancies.all():
            request.user.saved_vacancies.remove(vacancy)
        else:
            request.user.saved_vacancies.add(vacancy)

        return redirect(reverse("employers:vacancies_detail", args=[pk]))


class SavedVacanciesView(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = "candidates/saved_vacancies.html"
    context_object_name = "vacancies"
    paginate_by = 7

    def get_queryset(self):
        return self.request.user.saved_vacancies.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_paginated"] = context["page_obj"].has_other_pages()
        return context


class ApplicationsView(LoginRequiredMixin, ListView):
    template_name = "candidates/applications.html"
    context_object_name = "applications"
    paginate_by = 20

    def get_queryset(self):
        return self.request.user.applications.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_paginated"] = context["page_obj"].has_other_pages()
        return context
