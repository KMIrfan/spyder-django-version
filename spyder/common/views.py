from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'commontemp/index.html')
def common_login(request):
    return render(request,'commontemp/login.html')
def common_sellerlogin(request):
    return render(request,'commontemp/sellerlogin.html')
def common_customersignup(request):
    return render(request,'commontemp/customersignup.html')
def common_sellersignup(request):
    return render(request,'commontemp/sellersignup.html')