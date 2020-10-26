from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home_page),
    path('product/',products_page),
    path('customer/',customer_page),
]
