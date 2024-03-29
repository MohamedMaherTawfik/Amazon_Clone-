from django.urls import path
from .views import ProductDetail,ProductList,BrandList,BrandDetail,quesryset_debug
from .api import Product_list_api,Product_Detail_api,ProductListApi,ProductDetailApi

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',quesryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    
    
    
    #Api
    path('api/list',ProductListApi.as_view()),
    path('api/list/<int:pk>',ProductDetailApi.as_view()),
    
]
