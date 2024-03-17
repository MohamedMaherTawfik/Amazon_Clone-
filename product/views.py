from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,ProductImages,Review,Brand
from  django.db.models import Q , F , Value
from  django.db.models.aggregates import Min,Max,Count,Avg,Sum

# Create your views here.

def quesryset_debug(request):
    #filter
    data=Product.objects.select_related('brand').all
    # data=Product.objects.filter(price__gt=20) #Greater than 
    # data=Product.objects.filter(price__gte=20)#Greater than or equal
    # data=Product.objects.filter(price__lt=20)#less than 
    # data=Product.objects.filter(price__lte=20)#less than or equal
    # data=Product.objects.select_related('brand').filter(price__range=(40,60))#less than or equal
    
    #navigate
    # data=Product.objects.filter(brand__name='john_Martin')
    # data=Product.objects.filter(brand__price__gt=35)
    
    #filter with text
    # data=Product.objects.filter(name__contains='br')
    # data=Product.objects.filter(name__startswith='a')
    # data=Product.objects.filter(name__endswith='e')
    # data=Product.objects.filter(tags__isnull=False)
    
    # filter datetime
    # data=Review.objects.filter(created_at__year=2023)
    # data=Review.objects.filter(created_at__month='june')
    
    #filter 2 values
    # data=Product.objects.filter(price__gt=80,quantity__lt=10)# And
    # data=Product.objects.filter(
    #    Q( price__gt=80)|  # ~ = Not
    #    Q(quantity__lt=10)
    #     )# OR
    # data=Product.objects.filter(
    #    ~Q( price__gt=80)|  # ~ = Not
    #    ~Q(quantity__lt=10)
    #     )# OR with Not
    
    #filter with field lookup
    # data=Product.objects.filter(price=F("quantity"))
    
    # Arrang products default=تصاعدي
    # data=Product.objects.all().order_by('name','quantity')#تصاعدي
    # data=Product.objects.all().order_by('name'reverse())#تنازلي
    # data=Product.objects.all().order_by('-name')# تنازلي
    
    # data=Product.objects.all().order_by('name',)[0]  #first
    # data=Product.objects.all().order_by('name',)[-1] #last
    # data=Product.objects.all().earliest('name',)  #first
    # data=Product.objects.all().latest('name',)    #last
    
    #slice
    # data=Product.objects.all()[:10]  
    # data=Product.objects.all()[10:50]   
    
    #Select columns
    # data=Product.objects.values('name','price') #as dictionary
    # data=Product.objects.values_list('name','price') # as list
    
    #remove duplicate
    # data=Product.objects.all().distinct()

    #return Specific Column
    # data=Product.objects.only('price','name')
    
    
    #But not 
    # data=Product.objects.defer('brand','sku')
    
    #Aggregation
    # data=Product.objects.aggregate(Sum('quantity'))
    # data=Product.objects.aggregate(Avg('price'))
    
    #annotate
    # data=Product.objects.annotate(price_with_taxis=F('price')*1.2)
    
    return render(request,'product/debug.html', {"data":data})


class ProductList(ListView):
    model=Product
    
    
class ProductDetail(DetailView):
    model=Product
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["reviews"] =Review.objects.filter(product=self.get_object()) 
        context["related_products"] =Product.objects.filter(brand=self.get_object().brand) 
        return context




class BrandList(ListView):
    model=Brand
    queryset=Brand.objects.annotate(product_count=Count('Product_brand')) # get by related name in models 
    
class BrandDetail(ListView):
    model=Product
    template_name='product/brand_detail.html'
    paginate_by=20
    
    def get_queryset(self): #override on queryset
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    #retreive new data on --> template 
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        context['brand']=Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    
    
# def brand_detail(request):
#     brands=Brand.objects.all #queryset
#     context={'data':brands} # Ccontext 
#     return render(request,'brands.html',context) 
    