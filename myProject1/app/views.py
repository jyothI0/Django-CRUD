from django.shortcuts import render,redirect
from .models import Members


# Create your views here.
def index(request):
    members = Members.objects.all()
    return render(request,'index.html',{'members':members})

def add(request):
    return render(request,'add.html')

def addrecord(request):
        id= request.POST['id']
        name = request.POST['name']
        age = request.POST['age']
        member = Members(id=id,name=name,age=age)
        member.save()
        return redirect('/')


def update(request,id):
    member = Members.objects.get(id=id)
    return render(request,'update.html',{'member':member})

def updaterecord(request,id):
    member = Members.objects.get(id=id)
    member.name = request.POST['name']
    member.age = request.POST['age']
    member.save()
    return redirect('/')

def delete(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('/')
    
