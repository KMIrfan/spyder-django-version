from django.shortcuts import render, redirect
from .models import product
from common.models import seller
from django.http import JsonResponse
from .decorator import auth_seller

# Create your views here.
@auth_seller
def reseller_index(request):
    seller_details = seller.objects.get(id=request.session['seller'])
    seller_image = seller_details.seller_image
    return render(request,'resellertemp/index.html',{'image':seller_image})
@auth_seller
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
@auth_seller
def reseller_profile(request):
    
    seller_profile=seller.objects.get(id=request.session['seller'])
    context = {
        'prof':seller_profile
    }

    return render(request,'resellertemp/profile.html',context)
@auth_seller
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
        stock=request.POST['stock']

        new_pro=product(protitle=protitle,category=category,proid=proid,prosubtitle=prosubtitle,proimg=proimg,price=price,prodesc=prodesc,seller_id=seller,stock=stock)
        new_pro.save()
        msg='Successfully Added'

    return render(request,'resellertemp/addproduct.html',{'message':msg})
@auth_seller
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
@auth_seller
def reseller_recentorders(request):
    return render(request,'resellertemp/recentorders.html')
@auth_seller
def reseller_updatestock(request):
    pro = product.objects.filter(seller_id=request.session['seller'])
    context = {
        'product':pro
    }
    return render(request,'resellertemp/updatestock.html',context)
@auth_seller
def reseller_update(request):
    sell = seller.objects.get(id=request.session['seller'])
    
    msg=''
    
    if request.method=='POST':
       
        fname = request.POST['fname']
        lname = request.POST['lname']
        bus = request.POST['bus']
        email = request.POST['email']
        num = request.POST['num']
        bank = request.POST['bank']
        ac = request.POST['ac']
        image=request.FILES['sellerpic']

        
        sell.seller_fname=fname
        sell.seller_lname=lname
        sell.seller_bus=bus
        sell.seller_email=email
        sell.seller_phn=num
        sell.bank=bank
        sell.seller_accnt=ac
        sell.seller_image=image
        sell.save()
        msg = 'Updated Successfully'
        return redirect('reseller:profile')
    context = {
        'updates':sell,
        'message':msg,
        'sell':sell
        
    }

    return render(request,'resellertemp/update.html',context)
@auth_seller
def stock_up(request):
    id = request.POST['pno']
    prod = product.objects.filter(id = id).values('protitle','stock')
    # serialized_data = [{'pid':p.id, 'pname':p.protitle, 'stock': p.stock } for p in prod]
    protitle = prod[0]['protitle']
    prostock = prod[0]['stock']
    context = {
        'protitle':protitle,
        'stock':prostock,
        
    } 
    
    return JsonResponse(context)
@auth_seller
def add_stock(request):
    new_stock =request.POST['new_stock']
    pno = request.POST['pno']
    prod = product.objects.get(id = pno)
    pro=prod.stock
    pro = pro + int(new_stock)
    product.objects.filter(id = pno).update(stock=pro)
    msg = 'Updated Successfully'
    context = {
        'message':msg,
    } 
    return JsonResponse(context)
@auth_seller
def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:index')

def masterpage(request):
    
    return render(request,'resellertemp/masterpage.html')
    


