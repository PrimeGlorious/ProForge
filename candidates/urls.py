from django.urls import path
from candidates.views import index, JobsListView, JobsDetailView

urlpatterns = [
    path("", index, name="index"),
    path("jobs/", JobsListView.as_view(), name="jobs_list"),
    path("jobs/<int:pk>/", JobsDetailView.as_view(), name="jobs_detail"),
]

app_name = "candidates"