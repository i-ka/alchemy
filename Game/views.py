from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from AlchemyCommon.models import Element, Category, UserProfile, Report
from alchemysite import settings
from .forms import RegisterForm, ReportForm
import json
# Create your views here.


def index(request):
    return render(request, 'Game/index.html', {"text": "1"})


def game_page(request):
    if request.user.is_authenticated():
        return render(request, 'Game/game.html')
    else:
        return redirect(reverse('game:index'))


@login_required()
def feedback(request):
    error = False
    if request.method == 'POST':
        report_form = ReportForm(request.POST, request.FILES)
        if (report_form['text'].value() != ''):
            newreport = Report(text=request.POST['text'], user=request.user)
            if (request.FILES.get('screenshot', False)):
                newreport.screenshot = request.FILES['screenshot']
            newreport.save()
            return redirect('/')
        else:
            error = 'Заполните текст жалобы/предложения'
    else:
        report_form = ReportForm()
    return render(request, 'Game/feedback.html', {'report_form': report_form, 'error': error})


def activation(request, activationToken):
    userProfile = get_object_or_404(UserProfile, activationToken=activationToken)
    user = userProfile.user
    user.is_active = True
    user.save()
    return render(request, 'Game/activation_success_notify.html')

def registration(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            for el in Element.objects.filter(first_recipe_el=0).filter(second_recipe_el=0):
                user.profile.open_elements.add(el)
            if not settings.EMAIL_CONFIRM:
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['pass1'])
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'Game/email_confirm_notify.html')
    else:
        form = RegisterForm()
    return render(request, 'Game/regform.html', {'form': form})


def login_view(request):
    if (not request.is_ajax()):
        return HttpResponseForbidden()
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


def get_user_open_element_list(request, category_id):
	if not request.user.is_authenticated:
		return HttpResponseForbidden()

	category_id = int(category_id)
	openElementsDict = {"elements": []}
	userOpenElements = request.user.profile.open_elements.all()
	for element in userOpenElements:
		if (element.category.id == category_id):
			openElementsDict['elements'].append(element.dict())
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
        element1 = int(request.POST.get('first_element', False))
        element2 = int(request.POST.get('second_element', False))
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

        if element1obj in userOpenElements.all() and element2obj in userOpenElements.all():
            result['success'] = True
            result['newElement'] = resultElement.dict()
            userOpenElements.add(resultElement)
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(json.dumps(result))
    return HttpResponseForbidden()
