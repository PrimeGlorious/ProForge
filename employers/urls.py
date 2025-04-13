from django.urls import path

from employers.views import (
    CompanyDetailView,
    VacanciesListView,
    VacanciesDetailView,
    CompanyCreateView,
)

urlpatterns = [
    path("companies/<int:pk>/", CompanyDetailView.as_view(), name="company_detail"),
    path("companies/create/", CompanyCreateView.as_view(), name="company_create"),
    path("vacancies/", VacanciesListView.as_view(), name="vacancies_list"),
    path("vacancies/<int:pk>/", VacanciesDetailView.as_view(), name="vacancies_detail"),
]

app_name = "employers"
