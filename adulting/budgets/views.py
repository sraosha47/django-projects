from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    return render(request, "budgets/index.html")