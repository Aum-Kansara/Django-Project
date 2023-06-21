from django.shortcuts import render,HttpResponse
from datetime import datetime
from demo.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'name': "Aum Kansara"
    }
    return render(request,"index.html",context=context)

def about(request):
    return render(request,"about.html")

def dresses(request):
    return render(request,"dresses.html")

def chaniya_choli(request):
    return render(request,"chaniya_choli.html")

def custom_design(request):
    return render(request,"custom_design.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        print(name,email,phone,desc)
        contact1=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact1.save()
        messages.success(request,'Your Message Submmited !')
    return render(request,"contacts.html")