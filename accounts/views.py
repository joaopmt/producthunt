from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']
        conf_pswd = request.POST['conf_password']
        try:
            user = User.objects.get(username=username)
            return render(request, 'accounts/signup.html', {'error':'Username already taken'})
        except User.DoesNotExist:
            if pswd == conf_pswd:
                user = User.objects.create_user(username, password=pswd)
                auth.login(request, user)
                return redirect('homepage')
            else:
                return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']
        user = auth.authenticate(username=username, password=pswd)
        if user is None:
            return render(request, 'accounts/login.html', {'error':'Authentication failed'})
        else:
            auth.login(request, user)
            return redirect('homepage')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')