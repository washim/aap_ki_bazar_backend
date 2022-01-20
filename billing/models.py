from django.db import models

INVOICE_STATUS = (
    ('processed', 'Processed'),
    ('disputed', 'Disputed'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
    ('dispatched', 'Dispatched'),
)

ATTRIBUTES = (
    ('Kg', 'Kg'),
    ('Piece', 'Piece')
)

class Shipping(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, default='')
    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=255, default='')
    ward_no = models.CharField(max_length=50, default='')
    pincode = models.CharField(max_length=10, default='')

    class Meta:
        ordering = ['created']


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    picture = models.CharField(max_length=255, default='')
    weight_attributes = models.CharField(max_length=10, choices=ATTRIBUTES, default='Kg')
    availability = models.IntegerField(default=0)
    purchase_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)

    @property
    def quantity(self):
        return 1

    @property
    def weight(self):
        return ""


class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, related_name='shipping')
    status = models.CharField(max_length=10, choices=INVOICE_STATUS, default='processed')
    status_message = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['created']

    def items_ordered(self):
        return Order.objects.filter(invoice=self.id)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField()
    weight = models.CharField(max_length=10, default='')