from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm

# Create your views here.


class UserLogin(LoginView):
    template_name: str = "blog/auth/login.html"


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated Successfully")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid User")
    else:
        form = LoginForm()
    return render(request, "blog/auth/login.html", {"form": form})
