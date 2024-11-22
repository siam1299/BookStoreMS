from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CreateUserForm


# Create your views here.
def user_signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "accounts/signup.html", {"signupform": form})


def user_logout(request):
    logout(request)
    return redirect("home")
