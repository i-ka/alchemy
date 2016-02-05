from django.shortcuts import render,redirect

from AlchemyCommon.models import Element

# Create your views here.

def index(request):
    all_elements = Element.objects.all()
    return render(request,'AlchemyAdmin/index.html',{
            'elements':all_elements,
        })

def remove_element(request,el_id):
    Element.objects.get(pk=el_id).delete()
    return redirect('/alch-admin')
    
        
