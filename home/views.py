from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import home.models

from home.models import Settings

from product.models import catagory

from product.models import product


def index(request):
    setting=Settings.objects.get(pk=1)
    category=catagory.objects.all()
    products_slider=product.objects.all().order_by('-id')[:4]
    page="home"
    context={'setting':Settings,
             'page':page,
             'products_slider':products_slider,
             'category':category}
    return render(request,'index.html',context)

def aboutus(request):
    setting=Settings.objects.get(pk=1)
    context={'setting':Settings}
    return render(request,'about.html',context)
def contactus(request):
    setting=Settings.objects.get(pk=1)
    context={'setting':Settings}
    return render(request,'contact.html',context)

def category_products(request,id,slug):
    setting=Settings.objects.get(pk=1)
    products=product.objects.filter(catagory_id=id)
    return HttpResponse(products)