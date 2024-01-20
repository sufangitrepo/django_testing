from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    qty = models.IntegerField()
    off = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class CategoryProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product')

    class Meta:
        unique_together = ('category', 'product', )
