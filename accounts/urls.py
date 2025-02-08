"""
URL configuration for gantavya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'), )
"""

from allauth.socialaccount.providers.google.views import oauth2_login, oauth2_callback
from django.conf.urls.static import static
from django.urls import path

from gantavya import settings
from . import views


urlpatterns = [
    path("accounts/google/login/", oauth2_login, name="google_login"),
    path("accounts/google/login/callback/", oauth2_callback, name="google_callback"),
    
    path("login/", views.login_view, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile_view, name="profile"),

    path('accounts/social/signup/', views.CustomSocialAccountSignupView.as_view(), name='socialaccount_signup'),
]