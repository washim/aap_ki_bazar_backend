from django.contrib import admin
from .models import Shipping, Product, Invoice, Order

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity', 'weight')

admin.site.site_header = "APP KI BAZAR"
admin.site.site_title = "APP KI BAZAR"