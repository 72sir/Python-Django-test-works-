# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestInDjango', '0002_auto_20170221_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Item')),
                ('birthday', models.DateField(blank=True)),
            ],
        ),
    ]
