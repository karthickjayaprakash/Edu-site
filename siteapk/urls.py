from django.urls.resolvers import URLPattern
from . import views
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path("",views.home,name="home"),
    path("materials/",views.materials,name="materials"),
    path("index/",views.index,name="index"),  
    path("menucard/",views.menucard,name="menucard"),
    path("forms/",views.forms,name="forms"),
    path("menucard/materials/",views.menucard,name="menucard"),
   
    
    
]