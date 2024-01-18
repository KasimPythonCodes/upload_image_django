from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.


def receipes(request):
    if request.method =="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        
        Receipe.objects.create( #yaha model ke ander data ko save karne ka code hai
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            
        )
        
        return redirect('/receipes')
    queryset=Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    return render(request,"receipes.html", {'a':queryset})

def update(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipes/')
 
    return render(request,'update.html',{'a':queryset})
    

def delete(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')


    
    





