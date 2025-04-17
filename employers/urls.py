from django.urls import path

from employers.views import (
    CompaniesDetailView,
    VacanciesListView,
    VacanciesDetailView,
    CompaniesCreateView,
    CompaniesManageView,
    CompaniesUpdateView,
    CompaniesDeleteView,
    VacanciesCreateView,
    VacanciesManageView,
    VacanciesDeleteView,
    VacanciesUpdateView,
    VacanciesModerateView
)

urlpatterns = [
    path("companies/<int:pk>/", CompaniesDetailView.as_view(), name="companies_detail"),
    path("companies/create/", CompaniesCreateView.as_view(), name="companies_create"),
    path("companies/manage/", CompaniesManageView.as_view(), name="companies_manage"),
    path("companies/<int:pk>/update/", CompaniesUpdateView.as_view(), name="companies_update"),
    path(
        "companies/<int:pk>/delete/",
        CompaniesDeleteView.as_view(),
        name="companies_delete"
    ),
    path("vacancies/", VacanciesListView.as_view(), name="vacancies_list"),
    path("vacancies/<int:pk>/", VacanciesDetailView.as_view(), name="vacancies_detail"),
    path("vacancies/create/", VacanciesCreateView.as_view(), name="vacancies_create"),
    path("vacancies/manage/", VacanciesManageView.as_view(), name="vacancies_manage"),
    path(
        "vacancies/<int:pk>/delete/",
        VacanciesDeleteView.as_view(),
        name="vacancies_delete"
    ),
    path(
        "vacancies/<int:pk>/update/",
        VacanciesUpdateView.as_view(),
        name="vacancies_update"
    ),
    path(
        "vacancies/<int:pk>/moderate/",
        VacanciesModerateView.as_view(),
        name="vacancies_moderate"
    ),
]

app_name = "employers"
