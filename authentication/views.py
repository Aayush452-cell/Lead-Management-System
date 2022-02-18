from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        userpass = request.POST['password']
        try:
            user_obj = authenticate(username=username, password=userpass)
            login(request, user_obj)
            request.session['username'] = username
            return HttpResponse("You are logged in !!!")
        except:
            return HttpResponse("Something went wrong")
    else:
        return render(request, 'login.html')

def user_logout(request):
    try:
        logout(request)
        return HttpResponse("You are logged OUT !!!")
    except:
        return HttpResponse("Something Went wrong")