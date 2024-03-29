from django.urls import path
from .views import ProductDetail,ProductList,BrandList,BrandDetail,quesryset_debug
from .api import Product_list_api,Product_Detail_api

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',quesryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    
    
    
    #Api
    path('api/list',Product_list_api),
    path('api/list/<int:product_id>',Product_Detail_api)
    
]
