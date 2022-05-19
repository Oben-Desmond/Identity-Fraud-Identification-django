from django.contrib import admin
from .models import AppTransactions, Client

# Register your models here.

admin.site.register(Client)
admin.site.register(AppTransactions)

