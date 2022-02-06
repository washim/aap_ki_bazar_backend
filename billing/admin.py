from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.urls import path
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from django.http import HttpResponse
from django.db.models import Sum, F
from rangefilter.filters import DateRangeFilter
from .models import Shipping, Product, Invoice, Order


class MyChangeList(ChangeList):
    def get_results(self, *args, **kwargs):
        super(MyChangeList, self).get_results(*args, **kwargs)
        total_sum = 0
        for invoice in self.result_list.all():
            try:
                total_sum += Order.objects.filter(invoice=invoice.id).aggregate(tot_sum=Sum(F('product__price') * F('quantity')))['tot_sum']
            
            except Exception:
                total_sum += 0
        
        self.total_sum = total_sum
        self.delivery_boy_commission = self.result_list.count() * 15


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address', 'ward_no', 'pincode')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight_attributes', 'availability', 'purchase_price', 'price', 'created')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'status', 'customer_name', 'address', 'ward', 'pincode', 'dbc', 'invoice_total', 'vieworder')
    list_filter = [('created', DateRangeFilter), 'status', 'type', 'dbc']
    date_hierarchy = 'created'
    change_list_template = 'change_list.html'
    search_fields = ['shipping__ward_no', 'dbc']
    actions = ['send_to_printer']

    def get_changelist(self, request):
        return MyChangeList

    def get_rangefilter_created_title(self, request, field_path):
        return 'By Created Date'

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