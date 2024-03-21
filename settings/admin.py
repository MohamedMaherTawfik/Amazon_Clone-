from django.contrib import admin
from .models import Company
# Register your models here.


class CompanyFields(admin.ModelAdmin):
    list_display=['name','linked_in_link','address','phones']
    list_filter=['name','linked_in_link','address']
    search_fields=['name','linked_in_link','address']

admin.site.register(Company,CompanyFields)