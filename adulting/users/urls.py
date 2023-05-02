from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("account/newuser", views.newuser_view, name="newuser"),
    path("account/created", views.create_view, name="create"),
    path("account/changed", views.change_view, name="change"),
    path("account/<str:username>", views.account_view, name="account"),
]