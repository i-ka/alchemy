from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AlchemyCommon.models import Element, Category
from .forms import ElementForm
import json
# Create your views here.


@login_required(login_url='/login/')
def index(request):
    all_elements = Element.objects.all()
    return render(request, 'AlchemyAdmin/index.html', {
            'elements': all_elements,
        })

def get_catigories(request):
    categories_dict = {"catigories": []}
    categories = Category.objects.all()
    for category in categories:
        categories_dict["catigories"].append({
            "id": category.id,
            "name": category.name
            })
    return HttpResponse(json.dumps(categories_dict))


def element_list(request, category_id):
    elements_dict = {"elements": []}
    elements = Category.objects.get(pk=category_id).element_set.all()
    for el in elements:
        elements_dict['elements'].append({
            'image': 'qwer.jpg',
            'name': el.name,
            'id': el.id
            })
    return HttpResponse(json.dumps(elements_dict))


def remove_element(request, el_id):
    element_to_delete = Element.objects.get(pk=el_id)
    conflict_elements = element_to_delete.check_on_delete()
    print(conflict_elements)
    if not conflict_elements:
        element_to_delete.delete()
        return redirect('/alch-admin')
    error = True
    return render(request, 'AlchemyAdmin/index.html', {
        'element_to_delete': element_to_delete,
        'error': error,
        'elements': conflict_elements
        })


def update_element(request, el_id):
    updated_element = Element.objects.get(pk=el_id)
    if request.method == 'POST':
        form = ElementForm(request.POST, instance=updated_element)
        if form.is_valid():
            form.save()
            return redirect('/alch-admin')
    else:
        form = ElementForm(instance=updated_element)
    return render(request, 'AlchemyAdmin/add_element_form.html', {
        'updated_element': updated_element,
        'form': form,
        'update': True
        })


def create_element(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alch-admin')
    else:
        form = ElementForm()
    return render(request, 'AlchemyAdmin/add_element_form.html', {
        'form': form,
        })
