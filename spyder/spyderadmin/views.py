from django.shortcuts import render, redirect
from common.models import seller, cust
from reseller.models import product
from .models import spyderadmin
from django.http import JsonResponse
from .decorator import auth_admin

# Create your views here.
@auth_admin
def spideradmin_index(request):
    return render(request,'spideradmintemp/index.html')
@auth_admin
def spideradmin_approveseller(request):
    sell = seller.objects.filter(status='pending')
    context = {
        'result':sell
    }
    return render(request,'spideradmintemp/approveseller.html',context)
def spideradmin_viewseller(request):
    sell = seller.objects.all()
  
   
    context = {
        'seller':sell
    }
    return render(request,'spideradmintemp/viewseller.html',context)
def spideradmin_viewcustomer(request):
    customer = cust.objects.all()
    context = {
        'customer':customer
    }
    return render(request,'spideradmintemp/viewcustomer.html',context)
def spideradmin_login(request):
    msg = ''
    if request.method == 'POST':
        usr_name = request.POST['usrname']
        pwd = request.POST['pwd']
        try:
            spy = spyderadmin(user_name = usr_name,pwd = pwd)
            request.session['spyder'] = spy.id
            return redirect('spyderadmin:index')
        except:
            msg = "Invalid Login"
    return render(request,'spideradmintemp/login.html')
def viewproducts(request):
    products = product.objects.all()
    context = {
        'products':products
    }
    return render(request,'spideradmintemp/viewproducts.html',context)
def logout(request):
    del request.session['spyder']
    request.session.flush()
    return redirect('common:index')

def removecustomer(request):
    msg = ''
    customer = cust.objects.all()
    if request.method == 'POST':
        select = request.POST['select']
        remvcust = cust.objects.filter(id=select)
        remvcust.delete()
        msg = 'Deleted'
    context = {
        'remove' : customer,
        'message': msg
    }
    return render(request,'spideradmintemp/removecustomer.html',context)
def removecust(request):
    id = request.POST['id']
    customer = cust.objects.filter(id=id).values('cust_fname')
    cust_fname = customer[0]['cust_fname']
    context = {
        'remove':cust_fname
    }
    return JsonResponse(context)

def removeproduct(request):
    msg = ''
    pro = product.objects.all()
    if request.method == 'POST':
        select = request.POST['select']
        pro = product.objects.filter(id=select)
        pro.delete()
        msg = 'Deleted Successfully'
    context = {
        'remove':pro,
        'message':msg
    }
    return render(request,'spideradmintemp/removepro.html',context)

def removepro(request):
    id = request.POST['id']
    pro = product.objects.filter(id = id).values('protitle')
    protitle = pro[0]['protitle']
    print(protitle)
    context = {
        'remove':protitle
    }
    return JsonResponse(context)
def removeseller(request):
    msg = ''
    sell = seller.objects.all()
    if request.method == 'POST':
        select = request.POST['select']
        sell = seller.objects.filter(id = select)
        sell.delete()
        msg = 'Deleted Successfully'
    context = {
        'remove':sell,
        'message':msg
    }
    return render(request,'spideradmintemp/removeseller.html',context)

def removesell(request):
    id = request.POST['id']
    sell = seller.objects.filter(id = id).values('seller_fname')
    sellname = sell[0]['seller_fname']
    
    context = {
        'remove':sellname
    }
    return JsonResponse(context)

def approveseller(request,sid):
    sell = seller.objects.filter(id = sid).update(status = 'Approved')
    msg = 'Approved'
   
    return redirect('spyderadmin:approveseller')

def rejectseller(request,sid):
    sell = seller.objects.filter(id = sid).update(status = 'Rejected')
    
    return redirect('spyderadmin:approveseller')
def masterpage(request):
    
    
    return render(request,'spideradmintemp/masterpage.html')