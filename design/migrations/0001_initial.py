# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 18:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Item')),
                ('group', models.BooleanField(default=False, verbose_name='Group')),
                ('brend', models.BooleanField(default=False, verbose_name='Brend')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0435\u0434\u0438\u043d\u0438\u0446\u044b, \u0440\u0443\u0431.')),
                ('brend', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brendProduct', to='design.Category')),
                ('group', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groupProduct', to='design.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Skidka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skidka', models.IntegerField(default=0)),
                ('inData', models.DateField(blank=True, null=True)),
                ('outData', models.DateField(blank=True, null=True)),
                ('brend', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brendSkidka', to='design.Category')),
                ('group', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groupSkidka', to='design.Category')),
                ('unitProduct', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='design.Product')),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
