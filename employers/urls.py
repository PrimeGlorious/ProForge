from django.urls import path

from employers.views import (
    CompanyDetailView,
    VacanciesListView,
    VacanciesDetailView,
    CompanyCreateView,
    ManageCompaniesView,
    EditCompanyView,
    DeleteCompanyView,
    VacanciesCreateView
)

urlpatterns = [
    path("companies/<int:pk>/", CompanyDetailView.as_view(), name="company_detail"),
    path("companies/create/", CompanyCreateView.as_view(), name="company_create"),
    path("companies/manage/", ManageCompaniesView.as_view(), name="manage_companies"),
    path("companies/edit/<int:pk>/", EditCompanyView.as_view(), name="edit_company"),
    path("companies/delete/<int:pk>/", DeleteCompanyView.as_view(), name="delete_company"),
    path("vacancies/", VacanciesListView.as_view(), name="vacancies_list"),
    path("vacancies/<int:pk>/", VacanciesDetailView.as_view(), name="vacancies_detail"),
    path("vacancies/create/", VacanciesCreateView.as_view(), name="vacancies_create"),
]

app_name = "employers"
