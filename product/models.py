from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

FLAG_TYPES=(
    ('new','new'),
    ('sale','sale'),
    ('feature','feature'),
)

# Create your models here.
class Product(models.Model):
    name=models.CharField(_('Name'),max_length=120)
    price=models.FloatField(_('Price'),)
    image=models.ImageField(_('Image'),upload_to='products')
    flag=models.CharField(_('Flag'),max_length=10,choices=FLAG_TYPES)
    sku=models.CharField(_('Sku'),max_length=12)
    subtitle=models.CharField(_('Subtitle'),max_length=120)
    description=models.TextField(_('Description'),max_length=40000)
    quantity=models.IntegerField(_('Quantity'),)
    brand=models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='Product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    
    
class ProductImages(models.Model):
    product=models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_image',on_delete=models.CASCADE)
    image=models.ImageField(_('Image'),upload_to='product_images')

class Brand(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    image=models.ImageField(_('Image'),upload_to='brand')
    
    def __str__(self):
        return str(self.name)
    
class Review(models.Model):
    user=models.ForeignKey(User,verbose_name=_('User'),on_delete=models.SET_NULL,related_name='review_author')
    product=models.ForeignKey(Product,_('Product'),related_name='product_review',on_delete=models.CASCADE)
    rate=models.IntegerField(_('Rate'))
    review=models.CharField(_('Review'),max_length=250)
    created_at=models.DateTimeField(_('Created_at'),default=timezone.now)
    
    def __str__(self):
        return str(self.user)

