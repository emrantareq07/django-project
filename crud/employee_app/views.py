from django.shortcuts import redirect, render
from .models import member

def index(request):
    mem=member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):    
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=member(firstName=x,lastName=y,country=z)
    mem.save()
    return redirect("/")
def delete(request,id):
    mem=member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first'] 
    y=request.POST['last']
    z=request.POST['country']
    mem=member.objects.get(id=id)
    mem.firstName=x
    mem.lastName=y
    mem.country=z
    mem.save()
    return redirect("/")