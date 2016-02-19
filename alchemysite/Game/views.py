from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return render(request,'Game/game.html')
    else:
        return render(request,'Game/index.html',{"text":"1"})
