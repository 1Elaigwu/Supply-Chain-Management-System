from django.db import models
from django.utils import timezone

# Define the choices for the status field
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.order_id}: {self.product_name} - {self.order_date} ({self.status})"

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    supplier_contact = models.CharField(max_length=100, blank=True, null=True)
    supplier_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.supplier_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_available = models.PositiveIntegerField()
    last_stock_update = models.DateTimeField(auto_now=True)

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity_shipped = models.PositiveIntegerField()
    shipment_date = models.DateField()

# Remove the previous definition of OrderHistory and replace it with the new one
class OrderHistory(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

# Add the new definition of Inventory
class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_available = models.PositiveIntegerField()
    last_stock_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} - Available: {self.quantity_available}"
