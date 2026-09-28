from django.shortcuts import render

from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return render(request , 'shop/index.html')

def about(request):
    return HttpResponse("this is about")


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