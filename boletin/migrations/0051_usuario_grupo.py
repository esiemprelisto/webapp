# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0050_auto_20180628_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.GrupoScout'),
        ),
    ]
