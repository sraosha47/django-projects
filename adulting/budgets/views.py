#from django.shortcuts import render, get_object_or_404
#from django.urls import reverse
from django.views import generic


from .models import Budget
from django.contrib.auth.models import User 

# Create your views here.
"""
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    else:
        budget_list = Budget.objects.all()
        context = {
            "budget_list": budget_list,
        }
        return render(request, context, "budgets/index.html")
"""

class IndexView(generic.ListView):
    template_name = "budgets/index.html"
    context_object_name = "budget_list"
    

    def get_queryset(self):
        return Budget.objects.filter(owner = self.request.user) 