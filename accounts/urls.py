from django.urls import path, include
from accounts.views import RegisterView, SwitchRoleView


urlpatterns = [
    path(
        "",
        include("django.contrib.auth.urls")
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
    path(
        "switch-role/",
        SwitchRoleView.as_view(),
        name="switch_role"
    ),
]

app_name = "accounts"
