# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0060_gruposcoutfalse'),
    ]

    operations = [
        migrations.AddField(
            model_name='gruposcoutfalse',
            name='apellidoJefe',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]