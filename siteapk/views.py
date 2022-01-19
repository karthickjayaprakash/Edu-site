from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from .forms import CustomerForm

# Create your views here.

def home(request):
    return render(request,'basic.html')

def materials(request):
    obj = book.objects.all()
    return render(request,'materials.html',{'obj':obj})

def index(request):
    return render(request,'index.html')

def menucard(request):
    return render(request,'menucard.html')

def forms(request):
    
    if request.method == 'POST':
        form = CustomerForm(request.POST) 
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'forms.html',{'form':form,'obj':obj})
    else:
        form=CustomerForm()
        return render(request,'forms.html',{'form':form})

         
         
   
    

    
