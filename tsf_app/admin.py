from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CustomerDetail)
admin.site.register(TransactionDetail)