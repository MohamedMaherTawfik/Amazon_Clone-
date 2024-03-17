from django.urls import path
from .views import ProductDetail,ProductList,BrandList,BrandDetail,quesryset_debug

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',quesryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    
]
