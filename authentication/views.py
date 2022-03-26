from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser,Leads
from django.http import HttpResponse
from datetime import datetime


def handler404(request,exception=None):
    return render(request, '404.html',status=404)

def index(request):
    if request.user.is_authenticated and request.method == 'POST':
        leads = Leads.objects.filter(sales_representative=request.user)
        id = request.POST['id']
        notes = request.POST['notes']
        lead = Leads.objects.get(id=id)
        lead.notes = notes
        lead.save()
        return render(request, 'User_list_page.html', {'leads': leads})
    elif request.user.is_authenticated:
        leads = Leads.objects.filter(sales_representative=request.user)
        return render(request, 'User_list_page.html', {'leads': leads})
    else:
        return HttpResponse("You are not Authorized to visit this page!!!")

def user_login(request):
    if request.user.is_authenticated:
        leads = Leads.objects.filter(sales_representative=request.user)
        return render(request, 'User_list_page.html', {'leads': leads})
    else:
        if request.method == 'POST':
            email = request.POST['email']
            userpass = request.POST['password']
            try:
                user_obj = authenticate(email=email, password=userpass)
                login(request, user_obj)
                request.session['email'] = email
                leads = Leads.objects.filter(sales_representative=request.user)
                return render(request, 'User_list_page.html', {'leads': leads})
            except:
                return HttpResponse("Something went wrong")
        else:
            return render(request, 'login.html')


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
        return redirect('login')
    except:
        return HttpResponse("Something Went wrong")


def filtering(request, pk):
    if request.method == 'GET':
        leads = Leads.objects.filter(status=pk , sales_representative=request.user)
        return render(request, 'User_list_page.html', {'leads': leads})
    else:
        return render(request, 'User_list_page.html')

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m:
        m = 12
    d = min(date.day,
            [31, 29 if y % 4 == 0 and not y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)


def analytics(request):
    if request.user.is_authenticated:
        ncold = len(Leads.objects.filter(status="cold", sales_representative=request.user,
                                         created_at__gte=monthdelta(datetime.now(), -3)))
        nhot = len(Leads.objects.filter(status="hot", sales_representative=request.user,
                                        created_at__gte=monthdelta(datetime.now(), -3)))
        nmed = len(Leads.objects.filter(status="med", sales_representative=request.user,
                                        created_at__gte=monthdelta(datetime.now(), -3)))
        nsold = len(Leads.objects.filter(status="sold", sales_representative=request.user,
                                        created_at__gte=monthdelta(datetime.now(), -3)))

        sold = Leads.objects.filter(status="sold")
        sold_dic = {}
        for solds in sold:
            if solds.sales_representative in sold_dic.keys():
                sold_dic[solds.sales_representative] += 1
            else:
                sold_dic[solds.sales_representative] = 1

        sold_dic = sorted(sold_dic.items(), key=lambda x: x[1], reverse=True)[
                   :10]  # Sorted in descending order according to values

        n = ncold + nmed + nhot + nsold
        params = {'n': n, 'ncold': ncold, 'nhot': nhot, 'nmed': nmed, 'sold_dic': sold_dic}
        print(ncold, nhot, nmed, sold_dic, params)
        return render(request,'analytics.html', {'params': params})
    else:
        return HttpResponse("Not authorized to view this page")
