from django.shortcuts import render

# Create your views here.
def spideradmin_index(request):
    return render(request,'spideradmintemp/index.html')
def spideradmin_approveseller(request):
    return render(request,'spideradmintemp/approveseller.html')
def spideradmin_viewseller(request):
    return render(request,'spideradmintemp/viewseller.html')
def spideradmin_viewcustomer(request):
    return render(request,'spideradmintemp/viewcustomer.html')