from unicodedata import name
from .views import *
from django.urls import path,include

urlpatterns = [
    path('',Home,name='home'),
    path('customers/',customers,name='customers')
]