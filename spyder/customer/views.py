from django.shortcuts import render

# Create your views here.
def customer_index(request):
    return render(request,'customertemp/index.html')
def customer_product(request):
    return render(request,'customertemp/productdetails.html')