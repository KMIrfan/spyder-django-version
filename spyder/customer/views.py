from django.shortcuts import render

# Create your views here.
def customer_index(request):
    return render(request,'customertemp/index.html')
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