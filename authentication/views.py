from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.http import HttpResponse


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        userpass = request.POST['password']
        try:
            user_obj = authenticate(email=email, password=userpass)
            login(request, user_obj)
            request.session['email'] = email
            return HttpResponse("You are logged in !!!")
        except:
            return HttpResponse("Something went wrong")
    else:
        return render(request, 'User_list_page.html')


def user_register(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone_no = request.POST['phone']
        userpass = request.POST['password']
        try:
            user = CustomUser.objects.create_user(email=email, first_name=fname, last_name=lname, password=userpass,
                                              phone_no=phone_no)
            return redirect('login')
        except:
            return HttpResponse("Something went wrong")
    return render(request, 'register.html')


def user_logout(request):
    try:
        logout(request)
        return HttpResponse("You are logged OUT !!!")
    except:
        return HttpResponse("Something Went wrong")
