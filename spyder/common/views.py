from django.shortcuts import render,redirect
from .models import cust,seller
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from reseller.models import product
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
from django.http import HttpResponse

# Create your views here.
logger = logging.getLogger('django')

def info (request) :
    logger.info("this is info message") 
    return HttpResponse ("info")

def common_index(request):
    logger.info("this is info message") 
    pro = product.objects.all()
    context = {
        'product':pro
    }
    return render(request,'commontemp/index.html',context)
def common_login(request):
    msg=''
    if request.method=='POST':
        cust_id=request.POST['custid']
        cust_pwd=request.POST['pwd']
        try:
            customer=cust.objects.get(cust_fname=cust_id,cust_pass=cust_pwd)
            request.session['customer'] = customer.id
            return redirect('customer:index')

        except Exception as e:
            print (e)
            msg="invalid credentials"
    return render(request,'commontemp/login.html')
def common_sellerlogin(request):
    msg = ''
    if request.method=='POST':
        seller_id=request.POST['sellerid']
        seller_pwd=request.POST['pwd']
        try:
            sell = seller.objects.get(seller_usr=seller_id,seller_pass=seller_pwd,status='Approved')
            request.session['seller'] = sell.id
            return redirect('reseller:index')

        except Exception as e:
            print (e)
            msg="invalid credentials"
    return render(request,'commontemp/sellerlogin.html',{'message':msg})
    
def common_customersignup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        email=request.POST['email']
        num=request.POST['num']
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
        house=request.POST['house']
        pin=request.POST['pin']
        post=request.POST['post']
        landmark=request.POST['landmark']
        dist=request.POST['dist']
        state=request.POST['state']
        new_cust=cust(cust_fname=fname,cust_lname=lname,gender=gender,cust_email=email,cust_phn=num,cust_pass=pwd,cust_cnfrmpass=cpwd,state=state,dist=dist,pin=pin,post=post,house=house,landmark=landmark)
        new_cust.save()
    return render(request,'commontemp/customersignup.html')

def common_sellersignup(request):
    msg=''
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        bus=request.POST['bus']
        email=request.POST['email']
        num=request.POST['num']
        bank=request.POST['bank']
        ac=request.POST['ac']
        image=request.FILES['sellerpic']
        seller_usr=randint(1111,9999)
        pwd='sel-' + str(seller_usr) + '-' + num[6:10]
        new_sell=seller(seller_fname=fname,seller_lname=lname,seller_bus=bus,seller_email=email,seller_phn=num,seller_pass=pwd,bank=bank,seller_accnt=ac,seller_image=image,seller_usr=seller_usr )
        new_sell.save()
        msg = 'Created Successfully'
        # email_subject='Account User name and Password'
        # email_content='user name:'+ str(seller_usr) +'password: ' + pwd
        
        # send_mail(
        #     email_subject,
        #     email_content,
        #     settings.EMAIL_HOST_USER,
        #     [email,]
        # )
    return render(request,'commontemp/sellersignup.html', {'message':msg})

def emailverification(request):
    msg = ''
    emailver = request.POST['demo']
    customer = cust.objects.filter(cust_email=emailver).exists()
    if customer:
        msg = '* Email is already exist'
    context = {
        'message':msg,
    }
    return JsonResponse(context)

def masterpage(request):
    return render(request,'commontemp/masterpage.html')

def selleremailverification(request):
    msg = ''
    emailver = request.POST['demo']
    customer = seller.objects.filter(seller_email=emailver).exists()
    if customer:
        msg='* Email is already exist'
    context = {
        'message':msg,
    }
    return JsonResponse(context)
@api_view(['GET'])
def index(request):
    return Response('Congratulations, you have created an API')

@api_view(['GET'])
def floattest(request):
    a = 4.5
    print (a)
    return Response(float)

