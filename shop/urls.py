from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("" ,views.index , name="shopHome"),
     path("about/" ,views.about , name="About Us"),
     path("tracking/" ,views.tracker , name="tracking status"),
     path("contact/" ,views.contact , name="Contact Us"),
     path("productview/" ,views.prodview , name="search"),
     path("search/" ,views.search , name="search"),
     path("checkout/" ,views.checkout , name="checkout")
]
