# coding: utf-8
from __future__ import unicode_literals

from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _

from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(_(u'Группа товара'), max_length=64)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Группа')
    name = models.CharField('Название товара', max_length=128)
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукция'



class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)

    def delete_real(self):
        super(CustomQuerySet, self).delete()



class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class Item(models.Model):
    name = models.CharField('Item', max_length=100)
    active = models.BooleanField('Active', default=True)
    objects = CustomManager()


class Person(models.Model):
    name = models.CharField('Item', max_length=100)
    birthday = models.DateField(null=True, blank=False)