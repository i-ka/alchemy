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
    
def create_element(request):
    status = False
    if request.method == 'POST':
        new_el = Element(
            name = request.POST['name'],
            first_recipe_el = int(request.POST['first_recipe_el']),
            second_recipe_el = int(request.POST['second_recipe_el']),
            discription = request.POST['discription'],
            )
        if new_el.check_conflict():
            new_el.save()
            status = 'Элемент добавлен'
        else:
            status = 'Ошибка:элемент из рецепта не существует!'
    return render(request,'AlchemyAdmin/add_element_form.html',{
        'status':status,
        })
