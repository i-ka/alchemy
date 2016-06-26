from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from AlchemyCommon.models import Element
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        return render(request, 'Game/game.html')
    else:
        return render(request, 'Game/index.html', {"text": "1"})


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                )
            user.set_password(form.cleaned_data['pass1'])
            user.save()
            for el in Element.objects.filter(first_recipe_el=0).filter(second_recipe_el=0):
                user.profile.open_elements.add(el)
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['pass1']
                )
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'Game/regform.html', {'form': form})
