# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0008_bebida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='pizzas.Pizza')),
            ],
        ),
    ]
