from django.shortcuts import render

# Create your views here.
def reseller_index(request):
    return render(request,'resellertemp/index.html')
def reseller_changepassword(request):
    return render(request,'resellertemp/changepassword.html')
def reseller_profile(request):
    return render(request,'resellertemp/profile.html')
def reseller_addproduct(request):
    return render(request,'resellertemp/addproduct.html')
def reseller_productcatelogue(request):
    return render(request,'resellertemp/productcatelogue.html')
def reseller_recentorders(request):
    return render(request,'resellertemp/recentorders.html')
def reseller_updatestock(request):
    return render(request,'resellertemp/updatestock.html')

