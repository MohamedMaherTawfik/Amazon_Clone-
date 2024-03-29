from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Product



@api_view(['GET'])
def Product_list_api(request):
    Products=Product.objects.all()[:20] #return as a list
    data=ProductSerializers(Products,many=True,context={'request':request}).data  #return as a Json 
    return Response({'products':data})
    

@api_view(['GET'])
def Product_Detail_api(request,product_id):
    Products=Product.objects.get(id=product_id) #return as a list
    data=ProductSerializers(Products,context={'request':request}).data  #return as a Json 
    return Response({'products':data})
    
    