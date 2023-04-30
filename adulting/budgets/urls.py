from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views

app_name = "budgets"

urlpatterns = [
    path("<str:username>", views.index, name="index"),
    path("categories/<str:username>/<str:budget_name>/<int:budget_id>", views.categories, name="categories"),
    path("entries/<str:username>/<str:category_name>/<int:category_id>", views.entries, name="entries"),
]