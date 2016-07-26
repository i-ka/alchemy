from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from .forms import RegisterForm
from AlchemyCommon.models import Element, Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        return render(request, 'Game/game.html')
    else:
        return render(request, 'Game/index.html', {"text": "1"})


def registration(request):
    if request.user.is_authenticated():
    	return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['pass1'])
            user.save()
            for el in Element.objects.filter(first_recipe_el=0).filter(second_recipe_el=0):
                user.profile.open_elements.add(el)
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['pass1'])
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'Game/regform.html', {'form': form})


def login_view(request):
	return HttpResponseForbidden() # this page forbidden for awhile
	result = ''
	if request.user.is_authenticated():
		result = 'alreadyLogIn'
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request,user)
				result = 'success'
			else:
				result = 'userNotActive'
		else:
			result = 'wrongPassOrLogin'
	else: 
		return HttpResponseForbidden()
	return HttpResponse(result)


def get_categories(request):
    categories_dict = {"categories": []}
    categories = Category.objects.all()
    for category in categories:
        categories_dict["categories"].append({
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


def get_user_open_element_list(request, category_id):
	if not request.user.is_authenticated:
		return HttpResponseForbidden()

	category_id = int(category_id)
	openElementsDict = {"elements": []}
	userOpenElements = request.user.profile.open_elements.all()
	for element in userOpenElements:
		if (element.category.id == category_id):
			openElementsDict['elements'].append({
				'id': element.id,
				'name': element.name,
				'image': 'element.image'
				})
	return HttpResponse(json.dumps(openElementsDict))



def check_element(request):
    """
    return json

    {
        'success': bool
        'newElement':{
            'id':
            'name':
            'image':
        }
    }

    """
    if (not request.user.is_authenticated):
        return HttpResponseForbidden()

    if request.method == 'POST':
        result = {'success': False}
        element1 = int(request.POST['first_element'])
        element2 = int(request.POST['second_element'])
        if element1 > element2:
            element1, element2 = element2, element1
        try:
            element1obj = Element.objects.get(pk=element1)
            element2obj = Element.objects.get(pk=element2)
            resultElement = Element.objects.get(first_recipe_el=element1,
                                                second_recipe_el=element2)
        except Element.DoesNotExist:
            return HttpResponse(json.dumps(result))

        userOpenElements = request.user.profile.open_elements
        if resultElement in userOpenElements.all():
            return HttpResponse(json.dumps(result))

        if element1obj in userOpenElements.all() and element2obj in userOpenElements.all():
            result['success'] = True
            result['newElement'] = {'id': resultElement.id,
                                    'name': resultElement.name,
                                    'image': 'qwe.jpg'}
            userOpenElements.add(resultElement)
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(json.dumps(result))
    return HttpResponseForbidden()
