from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
def auth_admin (func) :
    def wrapper (request, *args, **kwargs):
        if 'spyder' in (request.session):
            return func (request, *args, **kwargs)
            
        else:
            return redirect('common:index')
    return wrapper