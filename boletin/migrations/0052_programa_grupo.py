# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0051_usuario_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.GrupoScout'),
        ),
    ]
