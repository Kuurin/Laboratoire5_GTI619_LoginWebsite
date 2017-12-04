from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.groups.filter(name__icontains="Prepose aux clients residentiels").exists():
        return render(request,'prepresidentiels/home.html')
    elif request.user.groups.filter(name__icontains="Administrateur").exists():
        return render(request,'prepresidentiels/home.html')
    else:
        return render(request,'account/login.html')
