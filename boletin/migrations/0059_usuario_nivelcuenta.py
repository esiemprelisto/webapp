# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0058_remove_usuario_nivelnacional'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nivelCuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.nivelCuenta'),
        ),
    ]