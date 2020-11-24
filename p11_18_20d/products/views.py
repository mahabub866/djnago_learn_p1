from django.shortcuts import render, redirect,get_object_or_404
from .models import Products,Rproduct
from .froms import ProductFrom,RawFrom
# Create your views here.
def rawform_create(request):

    form=RawFrom()
    if request.method=="POST":
        form=RawFrom(request.POST)
        if form.is_valid():
            Rproduct.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context={
       "form":form
        }
    return render(request,"product/raw_product_create.html",context)

def product_create(request):
    obj=Products.objects.get(id=1)
    form=ProductFrom(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form=ProductFrom()

    context={
        'form':form
    }
    return render(request,"product/product_create.html",context)
def product(request,my_id):
    obj=get_object_or_404(Products,id=my_id)
    context={
        'object':obj
    }
    return render(request,"product/product1.html",context)
def rproduct(request,my_id):
    obj=get_object_or_404(Rproduct,id=my_id)
    context={
        'object':obj
    }
    return render(request,"product/product2.html",context)

def product_list(request):
    obj=Products.objects.all()
    obj1=Rproduct.objects.all()
    context={
        'obj_list':obj,
        'R_obj_list':obj1
    }
    return render(request,"product/product_list.html",context)
