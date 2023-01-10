from django.shortcuts import render
from common.models import cust
from reseller.models import product

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
def customer_product(request):
    return render(request,'customertemp/productdetails.html')
def customer_changepassword(request):
    return render(request,'customertemp/passwordchange.html')
def customer_profile(request):
    return render(request,'customertemp/profile.html')
def customer_mycart(request):
    return render(request,'customertemp/mycart.html')
def customer_myorder(request):
    return render(request,'customertemp/myorder.html')