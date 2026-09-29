from django.shortcuts import render

from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = list(Product.objects.all())
    # products = list(products.objects.filter(price__lt=500))

    # group products into slides of 3
    slides = [products[i:i + 3] for i in range(0, len(products), 3)]

    return render(request, 'shop/index.html', {'slides': slides})
   

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