from django.urls import path
from candidates.views import (
    index,
    about,
    profile,
    toggle_save_vacancy,
    saved_vacancies,
    apply,
    applications
)

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("profile/", profile, name="profile"),
    path(
        "toggle-save-vacancy/<int:pk>/",
        toggle_save_vacancy,
        name="toggle_save_vacancy"
    ),
    path("saved-vacancies/", saved_vacancies, name="saved_vacancies"),
    path("apply/<int:pk>/", apply, name="apply"),
    path("applications/", applications, name="applications"),
]

app_name = "candidates"
