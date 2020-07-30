from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from homeapp import*

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        #로그인 실패시 팝업창 띄우기

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'signup.html')