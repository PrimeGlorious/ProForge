from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from candidates.models import Vacancy, Company


def index(request: HttpRequest) -> HttpResponse:
    vacancies_count = Vacancy.objects.count()
    companies_count = Company.objects.count()
    context = {
        "vacancies_count": vacancies_count,
        "companies_count": companies_count,
    }
    return render(
        request,
        "candidates/index.html",
        context=context,
    )
