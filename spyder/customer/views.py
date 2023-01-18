from django.shortcuts import render,redirect
from common.models import cust
from reseller.models import product
from .models import cart
from django.http import JsonResponse
from .decorator import auth_customer

# Create your views here.
@auth_customer
def customer_index(request):
    customer_details = cust.objects.get(id=request.session['customer'])
    products=product.objects.all()
    
    customer_name = customer_details.cust_fname + ' ' + customer_details.cust_lname
    context = {
        'fname':customer_name,
        'product':products
    }
    return render(request,'customertemp/index.html',context)

@auth_customer
def customer_product(request,pid):
    pro_details = product.objects.get(id=pid)
    msg=''
    if request.method=='POST':
        item = cart.objects.filter(customer_id=request.session['customer'],product_id=pid).exists()
        if not item:
            new_cart = cart(customer_id = request.session['customer'],product_id = pid)
            new_cart.save()
            return redirect('customer:mycart')
        else:
            msg='Item already in the cart'
    context={
        'prodetails':pro_details,
        'message':msg
    }
    return render(request,'customertemp/productdetails.html',context)

@auth_customer
def customer_changepassword(request):
    error_msg=''
    success_msg=''
    if request.method=='POST':
        oldpwd = request.POST['oldpwd']
        newpwd = request.POST['newpwd']
        cnfrmpwd = request.POST['cnfrmpwd']
        if newpwd==cnfrmpwd:
            if len(newpwd) > 8:
                confirmation=cust.objects.get(id=request.session['customer'])
                if oldpwd == confirmation.cust_pass:
                    cust.objects.filter(id=request.session['customer']).update(cust_pass = newpwd)
                    success_msg = 'Your password is updated successfully'
                else:
                    error_msg='Your old password is incorrect'    
            else:
                error_msg='password should be minimum 8 characters'
        else:
            error_msg="Password does\'nt match"
        
    context={
        'error':error_msg,
        'success':success_msg
    }
    
    return render(request,'customertemp/passwordchange.html',context)

@auth_customer
def customer_profile(request):
    prof=cust.objects.get(id=request.session['customer'])
    context = {
        'prof':prof
    }
    return render(request,'customertemp/profile.html',context)

@auth_customer
def customer_mycart(request):
    
    user=request.session['customer']
    my_cart = cart.objects.filter(customer_id=user)
    
    context = {
        'cart':my_cart
    }
    return render(request,'customertemp/mycart.html',context)

@auth_customer
def customer_myorder(request):
    return render(request,'customertemp/myorder.html')

@auth_customer
def customer_update(request):
    sell = cust.objects.get(id=request.session['customer'])
    msg=''
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        email = request.POST['email']
        num = request.POST['num']
                
        sell.cust_fname=fname
        sell.cust_lname=lname
        sell.gender=gender
        sell.cust_email=email
        sell.cust_phn=num
        
        sell.save()
        msg = 'Updated Successfully'
        return redirect('customer:profile')
    context = {
        'updates':sell,
        'message':msg,
        'sell':sell
    }
    return render(request,'customertemp/update.html',context)

def get_total(request):
    msg=''
    pid = request.POST['pid'] #pid is the key passed from ajax request
    qty = request.POST['qty']
    prod = product.objects.filter(id = pid).values('price','stock')
    total_amount = int(qty) * prod[0]['price']
    current_stock = prod[0]['stock']
    if int(qty) > current_stock:
        msg = 'Out of stock'
    context = {
        'amount': total_amount,
        'message':msg
    }
     
    return JsonResponse(context)
def remove_cart(request,cid):
    item = cart.objects.get(id=cid)
    item.delete()
    return redirect('customer:mycart')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:index')

def buy(request,pid):
    
    my_cart = product.objects.filter(id=pid)
    context = {
        'cart':my_cart
    }
    return render(request,'customertemp/buy.html',context)
def masterpage(request):
    
    
    return render(request,'customertemp/masterpage.html')

    

