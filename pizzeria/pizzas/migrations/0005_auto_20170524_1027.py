# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_pizza_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]