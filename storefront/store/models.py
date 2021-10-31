from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateTimeCheckMixin, DateTimeField

# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    titel = models.CharField(max_length=40)


class Products(models.Model):
    titel = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    Promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBRESHIP_BRONZE = 'B'
    MEMBRESHIP_SILVER = 'S'
    MEMBRESHIP_GOLD = 'G'

    MEMBRESHIP_CHOICES = [
        (MEMBRESHIP_BRONZE, 'Bronze'),
        (MEMBRESHIP_SILVER, 'Silver'),
        (MEMBRESHIP_GOLD, 'Gold')

    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    brith_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBRESHIP_CHOICES, default=MEMBRESHIP_BRONZE)


class Order(models.Model):
    PAYMENT_Pending = 'P'
    PAYMENT_Complete = 'C'
    PAYMENT_Failed = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_Pending, 'pending'),
        (PAYMENT_Complete, 'Complete'),
        (PAYMENT_Failed, 'Failed')

    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, Choices=PAYMENT_STATUS, default=PAYMENT_Pending)
    Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItem (models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    Products = models.ForeignKey(Products, on_delete=models.PROTECT)


class Cart (models.Model):
    Created_at = models.DateTimeField(auto_now_add=True)


class CartItem (models.Model):
    quantity = models.PositiveSmallIntegerField()
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Products = models.ForeignKey(Products, on_delete=models.CASCADE)
