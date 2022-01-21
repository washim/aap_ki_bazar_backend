from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from django.http import HttpResponse
from .models import Shipping, Product, Invoice, Order


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address', 'ward_no', 'pincode')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight_attributes', 'availability', 'purchase_price', 'price', 'created')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'customer_name', 'address', 'ward', 'pincode', 'created', 'vieworder')
    list_filter = ['status']
    list_editable = ['status']
    search_fields = ['shipping__ward_no']
    actions = ['send_to_printer']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('details/<int:pk>', self.items_ordered),
        ]
        return my_urls + urls

    def items_ordered(self, request, pk):
        order = get_object_or_404(Invoice, id=pk)
        context = dict(self.admin_site.each_context(request), order=order)
        return TemplateResponse(request, "vieworder.html", context)

    def vieworder(self, invoice):
        return format_html("<a href='details/{}'>View Orders</a>", invoice.id)

    def customer_name(self, invoice):
        return invoice.shipping.name + '(' + invoice.shipping.mobile + ')'

    def address(self, invoice):
        return invoice.shipping.address
    
    def ward(self, invoice):
        return invoice.shipping.ward_no

    def pincode(self, invoice):
        return invoice.shipping.pincode

    @admin.action(description='Send to printer')
    def send_to_printer(self, request, queryset):
        response = HttpResponse()
        for invoice in queryset:
            invoice_total = 0
            response.write("<div>-------------------------------------------</div>")
            response.write("<div>Invoice ID: %s</div>" % invoice.id)
            response.write("<div>Customer Details: %s, %s, %s, %s</div>" % (invoice.shipping.name, invoice.shipping.mobile, invoice.shipping.address, invoice.shipping.ward_no))
            response.write("<div>Items</div>")
            response.write("<div>-------------------------------------------</div>")
            for order in Order.objects.filter(invoice=invoice.id):
                total = order.quantity * order.product.price
                invoice_total += total
                response.write("<div>%s x %s per %s %s %s</div>" % (order.quantity, order.product.price, order.product.weight_attributes, order.product.name, total))
            response.write("<div><b>Total:</b> %s</div>" % invoice_total)
            response.write("<div>-------------------------------------------</div>")
        return response

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity')

admin.site.site_header = "APP KI BAZAR"
admin.site.site_title = "APP KI BAZAR"