# coding: utf-8

import sys
reload(sys)
import locale

from django.db.models import Count, Sum
from django.db.models import Prefetch
from django.shortcuts import render
from requestInDjango.models import Product, Category, Item, Person


# Create your views here.


def requestInDjango(request, *args):

    if args is None:
        args = {}

    requestAll = Product.objects.all()
    requestOne = Product.objects.filter(price__gte=100).order_by('category')
    requestOneCount = Category.objects.filter(product__price__gte=100).annotate(count=Count('product'),
                                                                                sum=Sum('product__price'))

    requestOneCountTwo = Category.objects.filter(product__price__gte=100).prefetch_related(
        Prefetch('product_set', queryset=Product.objects.filter(price__gte=100))).distinct()

    list = []

    for category in requestOneCountTwo:
        products = category.product_set.all()
        buf = {
            'name': category.name,
            'len': len(products)
        }
        list.append(buf)

    # Задание 2
    # То же самое, но оставить лишь категории, в которых строго больше 10 товаров
    # Добавил условия IF в шаблон html


    # Задание 3
    # Написать код python, который выводит в консоль перечень всех товаров.
    # Каждая строка должна содержать следующие данные:
    # 1. Создаем запрос к базе данных

    productsAll = Product.objects.all()

    sys.setdefaultencoding(locale.getpreferredencoding())

    for elem in productsAll:
        print (u'---------------------------------------------')
        print(u'1. Категория: ' + elem.category.name)
        print (u'2. Наименование товара: ' + elem.name)
        print (u'3. Цена товара: ' + elem.price.to_eng_string())

    print (Item.objects.all())
    Item.objects.filter(pk=2).delete()
    elem = Item.objects.get(pk=2)
    print (elem.active)

    Person.objects.create(name='Name 1')

    return render(request, 'requestInDjango.html', {'product': requestAll,
                                                    'requestOne': requestOne, 'requestOneCount': requestOneCount,
                                                    'requestOneCountTwo': requestOneCountTwo, 'buf': list})
