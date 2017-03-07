from django.contrib import admin

# Register your models here.
from design.models import Category, Product, Skidka


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'brend')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'brend', 'price')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)


class SkidkaAdmin(admin.ModelAdmin):
    list_display = ('skidka', 'inData', 'outData', 'unitProduct', 'group', 'brend', 'user')
    list_filter = ['skidka']
    search_fields = ['skidka']


admin.site.register(Skidka, SkidkaAdmin)



