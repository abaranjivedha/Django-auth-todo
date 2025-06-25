from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#Sign Up
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username =username).exists():
            messages.error(request, "User is already taken")
            return redirect('signup')
        User.objects.create_user(username=username, password=password)
        messages.success(request, "Successfully created")
        return redirect('login')
    return render(request, 'signup.html')

#Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html', {'username' : username})
        else:
            messages.error(request, 'Invalid')
            return redirect('login')
    return render(request, 'login.html')

#Home
@login_required
def home_redirect(request):
    return redirect('task_list')

#Logout
def user_logout(request):
    return render(request, 'signup.html')