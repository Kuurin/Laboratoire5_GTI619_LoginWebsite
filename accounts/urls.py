from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^(?:home)?$', views.home),
    url(r'^failedlogin/$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout')
]

#user authentification urls
