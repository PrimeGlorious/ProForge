from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from candidates.models import Vacancy
from employers.models import Company


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


def profile(request: HttpRequest) -> HttpResponse:
    current_user = request.user

    applications = current_user.applications.all().order_by("-created_at")
    vacancies_count = Vacancy.objects.filter(company__owner=current_user).count()

    context = {
        "applications": applications,
        "current_user": current_user,
        "vacancies_count": vacancies_count
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
            "employers:vacancies_detail",
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
            "employers:vacancies_detail",
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
