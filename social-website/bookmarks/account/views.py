from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.


# @login_required
def personal_account(request):
    return render(request, "accounts/profile/index.html", {"section": "profile"})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(  # authenticate the user against the database
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)  # set the user in the current session
                    return HttpResponse("Authenticated Successfully")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})
