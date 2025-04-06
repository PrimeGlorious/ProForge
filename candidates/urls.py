from django.urls import path
from candidates.views import index, JobsListView

urlpatterns = [
    path("", index, name="index"),
    path("jobs/", JobsListView.as_view(), name="jobs_list"),
]

app_name = "candidates"