from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializers,ProductDetailSerializers,BrandListSerializers,BrandDetailSerializers
from .models import Product,Brand
from rest_framework import generics



# @api_view(['GET'])
# def Product_list_api(request):
#     Products=Product.objects.all()[:20] #return as a list
#     data=ProductSerializers(Products,many=True,context={'request':request}).data  #return as a Json 
#     return Response({'products':data})
    

# @api_view(['GET'])
# def Product_Detail_api(request,product_id):
#     Products=Product.objects.get(id=product_id) #return as a list
#     data=ProductSerializers(Products,context={'request':request}).data  #return as a Json 
#     return Response({'products':data})
    

class ProductListApi(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializers
    
    
class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerializers
    
    
class BrandListApi(generics.ListCreateAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializers
    

class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerializers