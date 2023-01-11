from django.shortcuts import render,redirect
from common.models import cust
from reseller.models import product
from .models import cart

# Create your views here.
def customer_index(request):
    customer_details = cust.objects.get(id=request.session['customer'])
    products=product.objects.all()
    
    customer_name = customer_details.cust_fname + ' ' + customer_details.cust_lname
    context = {
        'fname':customer_name,
        'product':products
    }
    return render(request,'customertemp/index.html',context)
def customer_product(request,pid):
    pro_details = product.objects.get(id=pid)
    
    msg=''
    if request.method=='POST':
       
        item = cart.objects.filter(customer=request.session['customer'],product=pid).exists()
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
                    success_msg = 'Your password is changed successfully'
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
def customer_profile(request):
    return render(request,'customertemp/profile.html')
def customer_mycart(request):
    user=request.session['customer']
    my_cart = cart.objects.filter(customer_id=user)
    context = {
        'cart':my_cart
    }
    return render(request,'customertemp/mycart.html',context)
def customer_myorder(request):
    return render(request,'customertemp/myorder.html')