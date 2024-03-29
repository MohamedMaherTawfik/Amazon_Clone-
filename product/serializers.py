from rest_framework import serializers
from .models import Product,Brand


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"


class BrandDetailSerializers(serializers.ModelSerializer):
    products=ProductSerializers(source='Product_brand',many=True)
    
    class Meta:
        model=Brand
        fields="__all__"