from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from apps.users import views as user_views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("", include("apps.food.urls")),
    path("", include("apps.favorites.urls")),
    path("sentry-debug/", trigger_error),
]
