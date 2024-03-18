from django.contrib import admin
from .models import Product,ProductImages,Review,Brand
# Register your models here.

class ProductImagesTabular(admin.TabularInline):
    model=ProductImages
    

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','flag','price','quantity','brand']
    list_filter=['flag','brand']
    search_fields=['name','subtitle','description']
    inlines=[ProductImagesTabular]


class ReviewProduct(admin.ModelAdmin):
    list_display=['product','rate','created_at']
    list_filter=['product','rate']
    search_fields=['rate','user']
    
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Review,ReviewProduct)
admin.site.register(Brand)