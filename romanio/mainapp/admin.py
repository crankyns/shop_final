from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}


class SubCategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):

     prepopulated_fields = {"slug": ("title",)}




admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)




