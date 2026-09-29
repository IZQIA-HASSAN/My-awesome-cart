from django.shortcuts import render

from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4)-(n//4))
    allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

   

def about(request):
    return render(request , "shop/about.html" )


def tracker(request):
    return HttpResponse("this is tracker")

def search(request):
    return HttpResponse("this is search")

def prodview(request):
    return HttpResponse("this is prodview")

def checkout(request):
    return HttpResponse("this is checkout")

def contact(request):
    return HttpResponse("this is contact")

def displaydbData(request):
    products = Product.objects.all()
    return render(request  , 'shop/display.html' , {'products' : 'products'})