from django.urls import path, include
from accounts.views import RegisterView


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", RegisterView.as_view(), name="register"),
]

app_name = "accounts"
