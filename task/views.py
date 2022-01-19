from task.models import courses
from django.shortcuts import render
from django.http import HttpResponse



def course(request):
    obj = courses.objects.all()
    return render(request,'course.html',{'obj':obj})

def quiz(request):
    return render(request,'quiz.html')
    
