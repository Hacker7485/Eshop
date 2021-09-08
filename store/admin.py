from django.contrib import admin
from store.models import Product,Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','description','category','image','text']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']




admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
