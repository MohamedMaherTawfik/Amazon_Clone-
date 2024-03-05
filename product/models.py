from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

FLAG_TYPES=(
    ('new','new'),
    ('sale','sale'),
    ('feature','feature'),
)

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=120)
    price=models.FloatField()
    image=models.ImageField(upload_to='products')
    flag=models.CharField(max_length=10,choices=FLAG_TYPES)
    sku=models.CharField(max_length=12)
    subtitle=models.CharField(max_length=120)
    description=models.TextField(max_length=40000)
    quantity=models.IntegerField()
    brand=models.ForeignKey('Brand',related_name='Product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    
    
class ProductImages(models.Model):
    pass


class Brand(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='brand')
    
    def __str__(self):
        return str(self.name)
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='review_author')
    product=models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    rate=models.IntegerField()
    review=models.CharField(max_length=250)
    created_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user)

