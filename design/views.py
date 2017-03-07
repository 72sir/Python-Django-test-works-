# coding: utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render
from design.models import Product, Skidka


# Create your views here.


def design(request):
    # Доп информация показать скидки по пользователю
    skidkiUser = Skidka.objects.filter(user__isnull=False)
    # Запоминаем имеется ли скидка у пользователья
    searchSkidkaUser = None

    if request.user.is_active:
        try:
            searchSkidkaUser = Skidka.objects.get(user=request.user)
            # Если нашли скидку по пользователю то далее мы можем с ней работатьи
            # вычитать из товара или прибавить к максимальной скидке товара
            print (u'skidka user ', searchSkidkaUser.skidka)
        except ObjectDoesNotExist:
            searchSkidkaUser = None
            print (u'Skidki net')

    # Фильтруем данные сразу по цене
    productsPrice = Product.objects.filter(price__gte=1000, price__lte=10000)
    # инфо по всем товарам для сравнения
    products = Product.objects.all()
    # сортируем скидки по дате
    skidki = Skidka.objects.filter(inData__lte=timezone.now(), outData__gte=timezone.now())
    # Передаем данные в шаблон
    args = {
        # вся продукция
        'products': products,
        # Сортируем скидки по дате
        'skidkis': skidki,
        # Скидки которые не вошли по дате
        'skidkaNotDate': Skidka.objects.filter(Q(outData__lt=timezone.now()) | Q(inData__gt=timezone.now())),
        # Запоминаем имеется ли скидка у пользователья
        'searchSkidkaUser': searchSkidkaUser
    }

    # Создадим лист для создания данных на основе товара и максимальной скидки
    list = []

    # Перебираем весь товар
    for product in productsPrice:
        # Перебираем все скидки по товару
        # запоминаем скидку что бы сравнивать в цикле for
        bufSkidkaMax = 0
        # Сюда заносим число выбора максимальной скидки
        # 1 - еденицу продукции 2 -  группа товаров 3 - по брендам
        bufSkidkaInfo = None
        # Буфер для создания List
        buf = {}
        # берем 1 продукт и выясняем максимальную скидку
        for skidka in skidki:
            # Определяем максмальную скидку,
            # для этого создадим лист со скидками
            # и в нем уже сделаем выборку

            # скидка на еденицу продукции
            if skidka.unitProduct == product:
                if bufSkidkaMax < skidka.skidka:
                    bufSkidkaMax = skidka.skidka
                    bufSkidkaInfo = 1

            # скидкa по группе товаров
            elif skidka.group == product.group:
                if bufSkidkaMax < skidka.skidka:
                    bufSkidkaMax = skidka.skidka
                    bufSkidkaInfo = 2

            # запоминаем скидку по брендам
            elif skidka.brend == product.brend:
                if bufSkidkaMax < skidka.skidka:
                    bufSkidkaMax = skidka.skidka
                    bufSkidkaInfo = 3

        # Фильтруем данные с учетом скидки между 1000 и 10 000
        skidkaPrice = product.price - int(bufSkidkaMax)

        if 999 < skidkaPrice < 10001:
            buf['skidkaPrice'] = product.price - int(bufSkidkaMax)
            buf['bufSkidkaMax'] = bufSkidkaMax
            buf['bufSkidkaInfo'] = bufSkidkaInfo
            buf['name'] = product.name
            buf['price'] = product.price

            list.append(buf)

    # Сортируем массив по ценам с учетом вычита скидки
    list.sort(key=lambda x: x['skidkaPrice'])

    args['list'] = list
    args['listUser'] = skidkiUser

    return render(request, 'design.html', args)



