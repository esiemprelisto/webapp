# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0027_auto_20180624_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosmedicos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.Usuario'),
        ),
    ]