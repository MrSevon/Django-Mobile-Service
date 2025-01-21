from django.contrib import admin
from .models import Service, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'created_at', 'items', 'quantities')
    search_fields = ('customer_name', 'phone_number')
    list_filter = ('created_at',)