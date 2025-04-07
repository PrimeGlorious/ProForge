from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from candidates.models import Vacancy, Company


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


class JobsDetailView(DetailView):
    model = Vacancy
    context_object_name = "vacancy"
    template_name = "candidates/vacancies_detail.html"
