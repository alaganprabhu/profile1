from django.shortcuts import render,redirect
from .models import Data
from django.contrib import messages

# Create your views here.

def home(request):
    data=Data.objects.all()
    if(data!=""):
        return render(request,"home.html",{"datas":data})
    else:
        return render(request,"home.html",{})

def sub(request):
    return render(request,"suc.html")        
    
def add(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        message=request.POST['message']

        obj=Data()
        obj.Name=name
        obj.Email=email
        obj.Mobile=mobile
        obj.Message=message
        obj.save()
        data=Data.objects.all()
        messages.success(request,'Your Message Sent!')
        return redirect('sub')
    return render(request,"home.html")

def skill(request):
    return render(request,'skills.html')


