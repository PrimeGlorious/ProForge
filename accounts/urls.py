from django.urls import path, include
from accounts.views import RegisterView, switch_role


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", RegisterView.as_view(), name="register"),
    path("switch-role/", switch_role, name="switch_role"),
]

app_name = "accounts"
