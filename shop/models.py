from django.db import models
from polymorphic.models import PolymorphicModel  # https://django-polymorphic.readthedocs.io/en/stable/index.html (need to be declared as app)


# Base Product definition as Polymorphic Class
class Product(PolymorphicModel):
    creation_date = models.DateField()
    primary_color = models.CharField(max_length=100)
    secondary_color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    picture = models.ImageField()
    description = models.TextField()
    unitary_price = models.DecimalField(max_digits=6, decimal_places=2)


# Cap definition as child class Product
class Cap(Product):
    logo_color = models.CharField(max_length=100)


# Shirt definition as child class Product
class Shirt(Product):
    MAN = 'Man'
    WOMAN = 'Woman'
    UNISEX = 'Unisex'
    sizing_choice = [(MAN, 'Man'), (WOMAN, 'Woman'), (UNISEX, 'Unisex')]

    size = models.CharField(max_length=100)
    type_of_fabric = models.CharField(max_length=100)
    sizing = models.CharField(max_length=6, choices=sizing_choice, default=UNISEX)
    hasSleeves = models.BooleanField()


# Class to represent a Cart
class Cart(models.Model):
    creation_date = models.DateField(primary_key=True)

    @property
    def total_products(self):
        total_quantity = self.items_cart.aggregate(models.Sum('quantity'))
        return total_quantity['quantity__sum']


# Class to store the product and the quantity for a cart
class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='items_cart', on_delete=models.CASCADE)
    quantity = models.IntegerField()
