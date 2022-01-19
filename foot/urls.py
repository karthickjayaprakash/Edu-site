from django.urls.resolvers import URLPattern
from . import views
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("about/",views.about,name="about"),
    path("menucard/",views.menucard,name="menucard"),
    path("table/",views.table,name="table"),
    path("form/",views.form,name="form"),
    path("product/",views.product,name="product")

      
]