from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views

app_name = "budgets"

urlpatterns = [
    #path("", login_required(views.IndexView.as_view()) , name="index"),
    path("<str:username>", views.index, name="index"),
    path("<int:pk>/<str:name>/", login_required(views.CategoriesView.as_view()), name="categories"),
    path("<int:pk>/entries", login_required(views.EntriesView.as_view()), name="entries"),
]