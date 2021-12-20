from django.shortcuts import render , redirect
from django.contrib.auth.models import auth , User
from django.contrib import messages
from .forms import fmod
# Create your views here.
from .models import *

def simra(request):
    ab =akbar.objects.all()
    return render(request,"bolly.html",{"ab":ab})

def bollywood(request):
    a=akbar.objects.filter(category="bollywood")
    return render(request,"bolly.html",{"ab":a})

def hollywood(request):
    a = akbar.objects.filter(category="hollywood")
    return render(request,"holly.html",{"ab":a})

def tollywood(request):
    a = akbar.objects.filter(category="tollywood")
    return render(request,"tolly.html",{"ab":a})

def webseries(request):
    a = akbar.objects.filter(category="webseries")
    return render(request,"webs.html",{"ab":a})

def mdata(request,id):
    aas= akbar.objects.filter(id=id)
    return render(request,"mdata.html",{"ab":aas[0]})

def ddata(request,id):
    aas= akbar.objects.filter(id=id).delete()
    return render(request,"mdata.html",{"ab":aas[0]})

def frs(request):
        if request.method == 'POST':
            form =fmod(request.POST)
            if form.is_valid():
                form.save()
                return redirect('fo')
            else:
                return render(request,'fo.html')
        else:
            form = fmod()
            return render(request,'fo.html',{'form': form})

