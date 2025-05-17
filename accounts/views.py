from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.views import SignupView

from .forms import (
    LoginForm,
    PasswordChangeForm,
    ProfileForm,
    SetPasswordForm,
    SocialSignUpForm,
    UserSignUpForm,
)


def login_view(request):
    msg = None
    form = LoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_superuser:
                    return redirect("/admin/")

                return redirect("/")
            msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "pages/auth/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
        msg = "Form is not valid"
    else:
        form = UserSignUpForm()

    return render(
        request,
        "pages/auth/register.html",
        {"form": form, "msg": msg, "success": success},
    )


@login_required()
def logout_user(request):
    logout(request)
    return redirect("/")


@login_required()
def profile_view(request):
    msg = None
    form = ProfileForm(request.POST or None)

    if request.method == "POST":
        data = request.POST
        user = request.user

        print(user.check_password(data.get("password")))
        if user.check_password(data.get("password")):
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.phone_number = data.get("phone_number")
            user.address = data.get("address")
            if request.FILES.get("profile_picture"):
                user.profile_picture = request.FILES.get("profile_picture")
            user.save()

            return redirect("profile")
        else:
            msg = "Invalid password"
    else:
        user = request.user
        form = ProfileForm(instance=user)

    return render(
        request,
        "pages/profile.html",
        {"form": form, "msg": msg},
    )


def change_password(request):
    msg = None
    form = PasswordChangeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            msg = "Invalid password"
    else:
        form = PasswordChangeForm()


class CustomSocialAccountSignupView(SignupView):
    adapter_class = DefaultSocialAccountAdapter

    def get(self, request, *args, **kwargs):
        form = SocialSignUpForm()
        return render(request, "pages/auth/socialaccount_signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = SocialSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("/"))
        return render(request, "pages/auth/socialaccount_signup.html", {"form": form})
