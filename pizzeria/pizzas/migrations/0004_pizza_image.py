# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20170523_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]