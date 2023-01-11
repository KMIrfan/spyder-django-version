from django.shortcuts import render
from .models import product
from common.models import seller

# Create your views here.
def reseller_index(request):
    seller_details = seller.objects.get(id=request.session['seller'])
    seller_image = seller_details.seller_image
    return render(request,'resellertemp/index.html',{'image':seller_image})

def reseller_changepassword(request):
    error_msg=''
    success_msg=''
    if request.method=='POST':
        oldpwd = request.POST['oldpwd']
        newpwd = request.POST['newpwd']
        cnfrmpwd = request.POST['cnfrmpwd']
        if newpwd==cnfrmpwd:
            if len(newpwd) > 8:
                confirmation=seller.objects.get(id=request.session['seller'])
                if oldpwd == confirmation.seller_pass:
                    confirmation.seller_pass = newpwd
                    confirmation.save()
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

    return render(request,'resellertemp/changepassword.html',context)
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
    user=request.session['seller']
    products=product.objects.filter(seller_id=user)

    seller_details=seller.objects.get(id=request.session['seller'])
    seller_name=seller_details.seller_fname
    
    context = {
        
        'product':products,
        'fname':seller_name
    }
    
    

    return render(request,'resellertemp/productcatelogue.html',context)
def reseller_recentorders(request):
    return render(request,'resellertemp/recentorders.html')
def reseller_updatestock(request):
    return render(request,'resellertemp/updatestock.html')

