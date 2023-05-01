from django.shortcuts import render
#from django.urls import reverse
#from django.contrib.auth.models import User

from .models import Budget, Category, Entry

# Create your views here.

# View showing list of all budgets of the user
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

# View listing all the categories of a specific budget
def categories(request, username, budget_name, budget_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif not username == request.user.username:
        return render(request, "budgets/index.html", {
            "message": "Access denied. These are not the budgets you're looking for."
        })
    else:
        category_list = Category.objects.filter(budget_id=budget_id)
        context = {
            "category_list": category_list,
            "budget_name": budget_name
        }
        return render(request, "budgets/categories.html", context)

# View showing all the entries of a category
def entries(request, username, category_name, category_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif not username == request.user.username:
        return render(request, "budgets/index.html", {
            "message": "Access denied. These are not the budgets you're looking for."
        })
    else:
        entry_list = Entry.objects.filter(category_id=category_id)
        context = {
            "entry_list": entry_list,
            "category_name": category_name
        }
        return render(request, "budgets/entries.html", context)
