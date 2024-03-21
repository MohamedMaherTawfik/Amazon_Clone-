from django.shortcuts import render
from product .models import Product,Brand,Review
from django.db.models import Count
# Create your views here.
def home(request):
    brands=Brand.objects.all().annotate(product_count=Count('Product_brand'))
    sale_Products=Product.objects.filter(flag='sale')[:10]
    feature_Products=Product.objects.filter(flag='feature')[:6]
    new_Products=Product.objects.filter(flag='new')[:10]
    reviews=Review.objects.all()[:5]
    
    return render(request,'settings/home.html',{
        'brand':brands,
        'sale_products':sale_Products,
        'feature_products':feature_Products,
        'new_products':new_Products,
        'reviews':reviews
        
    })
    
    
