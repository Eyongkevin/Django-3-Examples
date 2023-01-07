from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("login-dj/", LoginView.as_view(), name="dj_login"),
    path("logout-dj/", LogoutView.as_view(), name="dj_logout"),
    path("profile/", views.personal_account, name="personal"),
    # change password urls
    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
