# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(related_name='pizzas', to='pizzas.Ingredient'),
        ),
    ]