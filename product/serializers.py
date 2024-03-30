from rest_framework import serializers
from .models import Product,Brand
from django.db.models.aggregates import Avg


class ProductListSerializers(serializers.ModelSerializer):
    avg_rate=serializers.SerializerMethodField()
    reviews_count=serializers.SerializerMethodField()
    price_with_tax=serializers.SerializerMethodField()
    
    class Meta:
        model=Product
        fields='__all__'
        
    def get_avg_rate(self,product):# Self = object
        avg= product.product_review.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result=0
            return result
        return avg['rate_avg']
    
    def get_reviews_count(self,product:Product):
        reviews=product.product_review.all().count()
        return reviews
    
    def get_price_with_tax(self,product:Product):
        return product.price*1.5
        
class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
    
        
class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"




class BrandDetailSerializers(serializers.ModelSerializer):
    products=ProductListSerializers(source='Product_brand',many=True)
    
    class Meta:
        model=Brand
        fields="__all__"