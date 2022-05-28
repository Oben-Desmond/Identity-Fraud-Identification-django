from django.contrib import admin
from .models import AppTransactions, Client, ReportedTransactions

# Register your models here.

admin.site.register(Client)
admin.site.register(AppTransactions)
admin.site.register(ReportedTransactions)

