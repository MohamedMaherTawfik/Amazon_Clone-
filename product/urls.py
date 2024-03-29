from django.urls import path
from .views import ProductDetail,ProductList,BrandList,BrandDetail,quesryset_debug
from .api import ProductListApi,ProductDetailApi,BrandListApi,BrandDetailApi

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',quesryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    
    
    
    #Api
    path('api/productlist',ProductListApi.as_view()),
    path('api/productlist/<int:pk>',ProductDetailApi.as_view()),
    path('api/brandlist',BrandListApi.as_view()),
    path('api/brandlist/<int:pk>',BrandDetailApi.as_view()),
    
]
