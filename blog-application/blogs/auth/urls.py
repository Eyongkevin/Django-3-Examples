from django.urls import path

app_name = "auth"
from . import views

urlpatterns = [path("login/", views.UserLogin.as_view(), name="login")]
