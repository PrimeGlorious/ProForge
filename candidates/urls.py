from django.urls import path
from candidates.views import (
    index,
    JobsListView,
    JobsDetailView,
    about,
    profile,
    toggle_save_vacancy,
    saved_vacancies,
    apply,
    applications
)

urlpatterns = [
    path("", index, name="index"),
    path("jobs/", JobsListView.as_view(), name="jobs_list"),
    path("jobs/<int:pk>/", JobsDetailView.as_view(), name="jobs_detail"),
    path("about/", about, name="about"),
    path("profile/", profile, name="profile"),
    path("toggle-save-vacancy/<int:pk>/", toggle_save_vacancy, name="toggle_save_vacancy"),
    path("saved-vacancies/", saved_vacancies, name="saved_vacancies"),
    path("apply/<int:pk>/", apply, name="apply"),
    path("applications/", applications, name="applications"),
]

app_name = "candidates"