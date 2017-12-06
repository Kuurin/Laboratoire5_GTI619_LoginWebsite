from django.shortcuts import render
from .models import prepaffaire 
from django.views import generic

def home(request):
    
    if request.user.groups.filter(name__icontains="Prepose aux clients daffaire").exists():
        listeClientx = prepaffaire.objects.all()
        return render(request,'prepaffaire/home.html', context={'listeClientx':listeClientx})
    elif request.user.groups.filter(name__icontains="Administrateur").exists():
        listeClientx = prepaffaire.objects.all()
        return render(request,'prepaffaire/home.html', context={'listeClientx':listeClientx})
    else:
        return render(request,'account/login.html')
        
        
    
