from django.shortcuts import render, get_object_or_404
#from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Budget, Category, Entry

# Create your views here.

def index(request, username):
    
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif not username == request.user.username:
        return render(request, "budgets/index.html", {
            "message": "Access denied. These are not the budgets you're looking for."
        })
    else:
        budget_list = Budget.objects.filter(owner = request.user)
        context = {
            "budget_list": budget_list
        }
        return render(request, "budgets/index.html", context)

def categories(request, budget_name, username):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif not username == request.user.username:
        return render(request, "budgets/index.html", {
            "message": "Access denied. These are not the budgets you're looking for."
        })
    else:
        budget_id = Budget.objects.filter(budget_text=budget_name)[0].id
        category_list = Category.objects.filter(budget_id=budget_id)
        budget_name=budget_name
        context = {
            "category_list": category_list,
            "budget_name": budget_name
        }
        return render(request, "budgets/categories.html", context)

def entries(request, category_name, username):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif not username == request.user.username:
        return render(request, "budgets/index.html", {
            "message": "Access denied. These are not the budgets you're looking for."
        })
    else:
        category_id = Category.objects.filter(category_text=category_name)[0].id
        entry_list = Entry.objects.filter(category_id=category_id)
        category_name=category_name
        context = {
            "entry_list": entry_list,
            "category_name": category_name
        }
        return render(request, "budgets/entries.html", context)
