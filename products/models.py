from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name