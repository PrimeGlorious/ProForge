from django.urls import path
from candidates.views import (
    IndexView,
    AboutView,
    ProfileView,
    ToggleSaveVacancyView,
    SavedVacanciesView,
    ApplyView,
    ApplicationsView
)

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index"
    ),
    path(
        "about/",
        AboutView.as_view(),
        name="about"
    ),
    path(
        "profile/",
        ProfileView.as_view(),
        name="profile"
    ),
    path(
        "toggle-save-vacancy/<int:pk>/",
        ToggleSaveVacancyView.as_view(),
        name="toggle_save_vacancy"
    ),
    path(
        "saved-vacancies/",
        SavedVacanciesView.as_view(),
        name="saved_vacancies"
    ),
    path(
        "apply/<int:pk>/",
        ApplyView.as_view(),
        name="apply"
    ),
    path(
        "applications/",
        ApplicationsView.as_view(),
        name="applications"
    ),
]

app_name = "candidates"
