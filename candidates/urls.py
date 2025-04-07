from django.urls import path
from candidates.views import index, JobsListView, JobsDetailView, about

urlpatterns = [
    path("", index, name="index"),
    path("jobs/", JobsListView.as_view(), name="jobs_list"),
    path("jobs/<int:pk>/", JobsDetailView.as_view(), name="jobs_detail"),
    path("about/", about, name="about"),
]

app_name = "candidates"