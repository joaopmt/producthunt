from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        pswd = request.POST['password']
        conf_pswd = request.POST['conf_password']
        if pswd == conf_pswd:
            username = request.POST['username']
            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/signup.html', {'error':'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username, password=pswd)
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    #TODO
    return render(request, 'accounts/signup.html')