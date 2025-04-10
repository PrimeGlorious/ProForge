from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, DetailView

from candidates.forms import CandidateRegistrationForm, VacancySearchForm
from candidates.models import Vacancy, Company, Candidate


def index(request: HttpRequest) -> HttpResponse:
    vacancies_count = Vacancy.objects.count()
    companies_count = Company.objects.count()
    candidates_count = get_user_model().objects.count()
    context = {
        "vacancies_count": vacancies_count,
        "companies_count": companies_count,
        "candidates_count": candidates_count,
    }
    return render(
        request,
        "candidates/index.html",
        context=context,
    )


def about(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "candidates/about.html"
    )


class JobsListView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "candidates/vacancies_list.html"
    paginate_by = 7

    def get_queryset(self):
        queryset = Vacancy.objects.all().order_by("-created_at")
        text = self.request.GET.get("text", "")

        if text:
            return queryset.filter(
                Q(title__icontains=text) | Q(description__icontains=text)
            )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsListView, self).get_context_data(**kwargs)

        text = self.request.GET.get("text", "")

        context["search_query"] = text
        return context


class JobsDetailView(DetailView):
    model = Vacancy
    context_object_name = "vacancy"
    template_name = "candidates/vacancies_detail.html"


class RegisterView(generic.CreateView):
    form_class = CandidateRegistrationForm
    success_url = reverse_lazy("candidates:index")
    template_name = "registration/signup.html"


def profile(request: HttpRequest) -> HttpResponse:
    current_user = request.user

    applications = current_user.applications.all().order_by("-created_at")

    context = {
        "applications": applications,
        "current_user": current_user,
    }

    return render(
        request,
        "candidates/profile.html",
        context=context,
    )


@login_required
def apply(
        request: HttpRequest,
        pk: int
) -> HttpResponse:
    vacancy = get_object_or_404(Vacancy, id=pk)

    if vacancy in request.user.vacancies.all():
        request.user.vacancies.remove(vacancy)
    else:
        request.user.vacancies.add(vacancy)

    return redirect(
        reverse(
            "candidates:jobs_detail",
            args=[pk]
        )
    )


@login_required
def toggle_save_vacancy(
        request: HttpRequest,
        pk: int
) -> HttpResponse:
    vacancy = get_object_or_404(Vacancy, id=pk)

    if vacancy in request.user.saved_vacancies.all():
        request.user.saved_vacancies.remove(vacancy)
    else:
        request.user.saved_vacancies.add(vacancy)

    return redirect(
        reverse(
            "candidates:jobs_detail",
            args=[pk]
        )
    )


@login_required
def saved_vacancies(request: HttpRequest) -> HttpResponse:
    vacancies = request.user.saved_vacancies.all().order_by("-created_at")
    paginator = Paginator(vacancies, 7)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {
        "vacancies": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "page_obj": page_obj,
    }

    return render(
        request,
        "candidates/saved_vacancies.html",
        context=context,
    )


@login_required
def applications(request: HttpRequest) -> HttpResponse:
    applications = request.user.applications.all().order_by("-created_at")
    paginator = Paginator(applications, 20)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {
        "applications": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "page_obj": page_obj,
    }

    return render(
        request,
        "candidates/applications.html",
        context=context,
    )
