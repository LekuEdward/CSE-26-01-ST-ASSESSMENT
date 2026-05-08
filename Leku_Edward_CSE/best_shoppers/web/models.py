import random
from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name