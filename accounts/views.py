from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import ( authenticate, get_user_model, login, logout )

def home (request):
    numbers = [1,2,3,4,5]
    name = 'Amelie'

    args = {'myName':name,'numbers': numbers}
    return render(request, 'accounts/home.html', args)
