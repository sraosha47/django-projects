from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")
    
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })

def account_view(request, username):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif not username == request.user.username and not request.user.is_superuser:
        return render(request, "users/user.html", {
            "message": "Access denied. That's not your account."
        })
    else:
        account = get_object_or_404(User, pk=request.user.id)
        context ={
            "account": account,
            "username": username
        }
        return render(request, "users/account.html", context)

def change_view(request):
    if request.method == "POST":
        user_id = request.user.id
        new = None
        new = User.objects.filter(id=user_id).get()
        username = request.POST["username"] 
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]  
        new.username = username
        new.first_name = request.POST["first_name"]
        new.last_name = request.POST["last_name"]
        new.email = request.POST["email"] 
        if password != confirmation:
            return render(request, "users/user.html", { "message": "Passwords do not match."} )
        elif len(password) > 0 :
            new.set_password(password)
            new.save()
            return HttpResponseRedirect(reverse("users:login"))
        else:
            new.save()
            return HttpResponseRedirect(reverse("users:index"))
    else:
        return render(request, "users/user.html")

def newuser_view(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
                "message": "Access denied. You need to log in first."
            })
    elif request.user.is_superuser:
        return render(request, "users/new_user.html")
    else:
        return render(request, "users/user.html", {
            "message": "You shall not pass."
        })
    
def create_view(request):
    if request.method == "POST":
        superuser = request.POST["superuser"] 
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]   
        if password == confirmation:
            if superuser == "YES":
                new_usr = User.objects.create_superuser(username, password=password)
                new_usr.first_name = request.POST["first_name"]
                new_usr.last_name = request.POST["last_name"]
                new_usr.email = request.POST["email"]
                new_usr.save()
                return HttpResponseRedirect(reverse("users:newuser"))
            else:
                new_usr = User.objects.create_user(username, password=password)
                new_usr.first_name = request.POST["first_name"]
                new_usr.last_name = request.POST["last_name"]
                new_usr.email = request.POST["email"]
                new_usr.save()
                return HttpResponseRedirect(reverse("users:newuser"))
    else:
        return render(request, "users/new_user.html")
