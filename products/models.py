# Django Imports
from django.db import models

# Own Imports
from products.helpers import ObjectTracker

# Account Imports
from accounts.models import User


class Product(ObjectTracker):
    title = models.CharField(max_length=100,help_text="The name of the product.")
    description = models.TextField(max_length=500, help_text="The description of the product.")
    price = models.FloatField(default=0.0, help_text="The price of the product.")
    quantity = models.IntegerField(default=0, help_text="How many of this product exists?")
    
    class Meta:
        verbose_name_plural = "products"
        db_table = "products"
        ordering = ["-date_created"]
        
    def __str__(self) -> str:
        return self.title
    

class OrderStatus(models.Choices):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class Order(ObjectTracker):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
    status = models.CharField(max_length=12, choices=OrderStatus.choices, default="pending")

    class Meta:
        verbose_name_plural = "orders"
        db_table = "orders"
        ordering = ["-date_created"]

    def __str__(self) -> str:
        return f"{self.user.fullname} order"


class PaymentStatus(models.Choices):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"

class Payment(ObjectTracker):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    has_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=8, choices=PaymentStatus.choices, default="pending")
    
    class Meta:
        verbose_name_plural = "payments"
        db_table = "payments"
        ordering = ["-date_created"]
        indexes = [
            models.Index(
                fields=[
                    "user", "order", 
                    "has_paid", "date_created"
                ]
            )
        ]
        
    def __str__(self) -> str:
        return f"{self.user.fullname} payment for #{self.order.uuid} order"