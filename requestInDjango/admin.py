from django.contrib import admin

# Register your models here.
from requestInDjango.models import Category, Item, Person
from requestInDjango.models import Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ['category']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Item)
admin.site.register(Person)


