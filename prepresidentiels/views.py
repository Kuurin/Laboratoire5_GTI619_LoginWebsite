from django.shortcuts import render
from .models import prepresidentiel
# Create your views here.

def home(request):
    if request.user.groups.filter(name__icontains="Prepose aux clients residentiels").exists():
        listeClientx = prepresidentiel.objects.all()
        return render(request,'prepresidentiels/home.html', context={'listeClientx':listeClientx})
    elif request.user.groups.filter(name__icontains="Administrateur").exists():
        listeClientx = prepresidentiel.objects.all()
        return render(request,'prepresidentiels/home.html',  context={'listeClientx':listeClientx})
    else:
        return render(request,'account/login.html')
