from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request,'about.html')

def menucard(request):
    return render(request,'menucard.html')

def table(request):
    return render(request,'table.html')

def form(request):
    return render(request,'formDA.html')

def product(request):
    return render(request,'product.html')