# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


# Категория
class Category(models.Model):
    # Наименование
    name = models.CharField('Item', max_length=100)
    # Группа предназначения
    group = models.BooleanField('Group', default=False)
    # Бренд
    brend = models.BooleanField('Brend', default=False)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'%s' % self.name


# Продукт
class Product(models.Model):
    # Наименование
    name = models.CharField('Product', max_length=130)
    # Группа предназначения
    group = models.ForeignKey('Category', null=True, blank=True, related_name='groupProduct')
    # Бренд
    brend = models.ForeignKey('Category', null=True, blank=True, related_name='brendProduct')
    # Цена
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукция'

    def __unicode__(self):
        return u'%s' % self.name


# Скидка
# В такой группе минус что можно заенсти данные без предназначения,
# это мы будем отслеживать в момет сохранения данных
class Skidka(models.Model):
    # Процент предоставляемой скидки
    skidka = models.IntegerField(default=0)
    # Дата с
    inData = models.DateField(default=timezone.now(), null=False, blank=False)
    # Дата до
    # * по умолчанию сделаем что акция действует неделю
    outData = models.DateField(default=timezone.now() + timezone.timedelta(days=7), null=False, blank=False)
    # ссылка на продукт
    unitProduct = models.ForeignKey('Product', null=True, blank=True)
    # Группа предназначения
    group = models.ForeignKey('Category', null=True, blank=True, related_name='groupSkidka')
    # Бренд
    brend = models.ForeignKey('Category', null=True, blank=True, related_name='brendSkidka')
    # Пользователь
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = u'Скидка'
        verbose_name_plural = u'Скидки'


