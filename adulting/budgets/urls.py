from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views

app_name = "budgets"

urlpatterns = [
    path("<str:username>", views.index, name="index"),
    path("categories/<str:username>/<str:budget_name>", views.categories, name="categories"),
    path("entries/<str:username>/<str:category_name>", views.entries, name="entries"),
]