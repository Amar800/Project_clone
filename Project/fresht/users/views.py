from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

def user_login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.warning(request,("Error, wrong user name/password"))
            return redirect("login")
    return render(request, "login.html",)

def user_logout(request):
    logout(request)
    return redirect("home")


