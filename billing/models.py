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

DELIVERY_BOY_CODE = (
    ('DBC-01', 'DBC-01'),
    ('DBC-02', 'DBC-02'),
    ('DBC-03', 'DBC-03'),
    ('DBC-04', 'DBC-04'),
    ('DBC-05', 'DBC-05'),
    ('DBC-06', 'DBC-06'),
    ('DBC-07', 'DBC-07'),
    ('DBC-08', 'DBC-08'),
    ('DBC-09', 'DBC-09'),
    ('DBC-10', 'DBC-10')
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

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    picture = models.ImageField()
    weight_attributes = models.CharField(max_length=10, choices=ATTRIBUTES, default='Kg')
    availability = models.FloatField(default=0.0)
    purchase_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)

    @property
    def quantity(self):
        return 1


class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, related_name='shipping')
    status = models.CharField(max_length=10, choices=INVOICE_STATUS, default='processed')
    dbc = models.CharField(max_length=10, choices=DELIVERY_BOY_CODE, default='DBC-01')

    class Meta:
        ordering = ['created']

    def items_ordered(self):
        return Order.objects.filter(invoice=self.id)

    @property
    def invoice_total(self):
        return Order.objects.filter(invoice=self.id).aggregate(tot_sum=models.Sum(models.F('product__price') * models.F('quantity')))['tot_sum']

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.FloatField()

    def __str__(self):
        return str(self.id)