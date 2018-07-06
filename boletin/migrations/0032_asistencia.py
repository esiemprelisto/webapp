# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0031_auto_20180625_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('asistio', models.BooleanField(choices=[(False, 'Ausente'), (True, 'Presente')])),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boletin.Usuario')),
            ],
        ),
    ]
