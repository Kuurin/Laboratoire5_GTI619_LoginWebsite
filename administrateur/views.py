from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.groups.filter(name__icontains="Administrateur").exists():
        return render(request,'administrateur/home.html')
    else:
        return render(request,'account/login.html')
