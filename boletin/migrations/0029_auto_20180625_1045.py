# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0028_datosmedicos_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosapoderado',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='datosmedicos',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='datospadres',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='da',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.DatosApoderado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='dm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.DatosMedicos'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='dp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.DatosPadres'),
        ),
    ]