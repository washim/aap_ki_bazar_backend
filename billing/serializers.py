from rest_framework import  serializers
from .models import Shipping, Product, Invoice, Order

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.ReadOnlyField()
    weight = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'