from django.shortcuts import render,redirect

from AlchemyCommon.models import Element
from .forms import ElementForm

# Create your views here.

def index(request):
    all_elements = Element.objects.all()
    return render(request,'AlchemyAdmin/index.html',{
            'elements':all_elements,
        })

def remove_element(request,el_id):
    Element.objects.get(pk=el_id).delete()
    return redirect('/alch-admin')

def update_element(request,el_id):
    if request.method == 'POST':
        return redirect('/alch-admin')
    
def create_element(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            new_element = Element(
                name = form.cleaned_data['name'],
                first_recipe_el = form.cleaned_data['first_recipe_el'],
                second_recipe_el = form.cleaned_data['second_recipe_el'],
                discription = form.cleaned_data['discription']
                )
            new_element.save()
    else:
        form = ElementForm()
    return render(request,'AlchemyAdmin/add_element_form.html',{
        'form':form,
        })
