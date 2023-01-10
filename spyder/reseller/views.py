from django.shortcuts import render
from .models import product
from common.models import seller

# Create your views here.
def reseller_index(request):
    seller_details = seller.objects.get(id=request.session['seller'])
    seller_image = seller_details.seller_image
    return render(request,'resellertemp/index.html',{'image':seller_image})

def reseller_changepassword(request):
    return render(request,'resellertemp/changepassword.html')
def reseller_profile(request):
    return render(request,'resellertemp/profile.html')
def reseller_addproduct(request):
    msg=''
    if request.method=='POST':
        protitle=request.POST['protitle']
        category=request.POST['category']
        proid=request.POST['proid']
        prosubtitle=request.POST['prosubtitle']
        proimg=request.FILES['proimg']
        price=request.POST['price']
        prodesc=request.POST['prodesc']
        seller=request.session['seller']

        new_pro=product(protitle=protitle,category=category,proid=proid,prosubtitle=prosubtitle,proimg=proimg,price=price,prodesc=prodesc,seller_id=seller)
        new_pro.save()
        msg='Successfully Added'

    return render(request,'resellertemp/addproduct.html',{'message':msg})
def reseller_productcatelogue(request):
    
    return render(request,'resellertemp/productcatelogue.html')
def reseller_recentorders(request):
    return render(request,'resellertemp/recentorders.html')
def reseller_updatestock(request):
    return render(request,'resellertemp/updatestock.html')

