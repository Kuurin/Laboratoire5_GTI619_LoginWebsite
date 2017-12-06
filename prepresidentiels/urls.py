from django.conf.urls import url, include
from django.shortcuts import render
from . import views

# Create your views here.


urlpatterns = [
    url(r'^$', views.home, name='prepresidentiels')
]
