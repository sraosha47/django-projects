from django.shortcuts import render, get_object_or_404
#from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Budget, Category

# Create your views here.

def index(request, username):
    
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    else:
        budget_list = Budget.objects.filter(owner = request.user)
        context = {
            "budget_list": budget_list,
            "username": username
        }
        return render(request, "budgets/index.html", context)

class CategoriesView(generic.DetailView):
    model = Budget
    template_name = "budgets/categories.html"

class EntriesView(generic.DetailView):
    model = Category
    template_name = "budgets/entries.html"
