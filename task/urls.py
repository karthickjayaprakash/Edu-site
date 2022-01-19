from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("course/",views.course,name="course"),
    path("quiz/",views.quiz,name="quiz")    
]